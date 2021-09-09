import os

import cv2
from PIL import Image

from scraper import this_month, next_month


class ImageMaker:
    """Класс принимает запись из БД и формирует изображение карточки с прогнозом погоды."""
    card_template_path = 'static/base.jpg'
    new_moon_template_path = 'static/old_moon.png'
    old_moon_template_path = 'static/new_new_moon.png'

    def __init__(self, db_row):
        self.db_row = db_row
        print(self.db_row)

    def draw_card(self):
        card_img = cv2.imread('static/base.jpg', cv2.IMREAD_COLOR) #TODO возвращает None

        font_scale = .9
        thickness = 1
        coord_table = ((120, 35), (50, 190), (270, 190), (50, 240), (120, 70))

        for res in self.db_row:
            date = res['date']
            title = res['title']

            logo = str

            if 'Новолуние' in title:
                moon = cv2.imread(self.new_moon_template_path, cv2.IMREAD_COLOR)
                logo = moon
            elif 'Полнолуние' in title:
                moon = cv2.imread(self.old_moon_template_path, cv2.IMREAD_COLOR)
                logo = moon

            self.paste_logo(card_img, logo)

            cv2.putText(card_img, date, coord_table[0], cv2.FONT_HERSHEY_COMPLEX, font_scale, thickness)
            cv2.putText(card_img, title, coord_table[4], cv2.FONT_HERSHEY_COMPLEX, font_scale, thickness)

            self.save_ready_card(card_img, date)

    def save_ready_card(self, card_img, date_str):
        save_path = f'static/{date_str}.jpg'
        cv2.imwrite(filename=save_path, img=card_img)
        img = Image.open(save_path)
        img.show()

    def paste_logo(self, card_img, logo_img):
        """Вставляет логотип погоды в изображение"""
        print(logo_img)
        rows, cols, channels = logo_img.shape
        roi = card_img[0:rows, 0:cols]
        sun_img_gray = cv2.cvtColor(logo_img, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(sun_img_gray, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        card_img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
        sun_img_fg = cv2.bitwise_and(logo_img, logo_img, mask=mask)
        dst = cv2.add(card_img_bg, sun_img_fg)
        card_img[0:rows, 0:cols] = dst


card_this_month = ImageMaker(this_month)
card_this_month.draw_card()