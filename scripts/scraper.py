from datetime import datetime

import requests
from bs4 import BeautifulSoup as bs4


def get_urls():
    today = datetime.today()
    year = today.year
    this_month = today.month
    next_month = this_month + 1
    this_month_url = f'https://ru.astro-seek.com/faza-luny-kalendar-lunnyh-faz-onlayn?' \
                     f'narozeni_city=Anapa%2C+Russia&narozeni_input_hidden=&narozeni_hidden_local_tz=1' \
                     f'&narozeni_stat_hidden=RU&narozeni_podstat_hidden=Krasnodarskiy&narozeni_podstat_kratky_hidden=' \
                     f'&narozeni_podstat2_kratky_hidden=&narozeni_podstat3_kratky_hidden=&narozeni_mesto_hidden=Anapa' \
                     f'&narozeni_den=&narozeni_mesic={this_month}&narozeni_rok={year}&tolerance=1&narozeni_sirka_stupne=44' \
                     f'&narozeni_sirka_minuty=53&narozeni_sirka_smer=0&narozeni_delka_stupne=37' \
                     f'&narozeni_delka_minuty=19&narozeni_delka_smer=0#select_local_tz_anchor'
    next_month_url = f'https://ru.astro-seek.com/faza-luny-kalendar-lunnyh-faz-onlayn?' \
                     f'narozeni_city=Anapa%2C+Russia&narozeni_input_hidden=&narozeni_hidden_local_tz=1' \
                     f'&narozeni_stat_hidden=RU&narozeni_podstat_hidden=Krasnodarskiy&narozeni_podstat_kratky_hidden=' \
                     f'&narozeni_podstat2_kratky_hidden=&narozeni_podstat3_kratky_hidden=&narozeni_mesto_hidden=Anapa' \
                     f'&narozeni_den=&narozeni_mesic={next_month}&narozeni_rok={year}&tolerance=1&narozeni_sirka_stupne=44' \
                     f'&narozeni_sirka_minuty=53&narozeni_sirka_smer=0&narozeni_delka_stupne=37' \
                     f'&narozeni_delka_minuty=19&narozeni_delka_smer=0#select_local_tz_anchor'
    return this_month_url, next_month_url


THIS_MONTH = [get_urls()[0]]
NEXT_MONTH = [get_urls()[1]]

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'user_agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
}


def scraper(URL):
    moon_data = []
    for i in URL:
        r = requests.get(i).text
        soup = bs4(r, 'lxml')
        block = soup.find('table', style='width: 100%; background: #BBBBBB;')
        phase = block.find_all('tr', class_='ruka')
        for i in phase:
            date = i.find('a').get_text()
            ph = i.find('td', style='padding: 0 5px 0 5px;').get_text()
            if 'Полнолуние' in ph:
                edit_phase = ph.replace('Полнолуниев', 'Полнолуние в')
                moon_data.append({'title': edit_phase, 'date': date})
            elif 'НОВОЛУНИЕ' in ph:
                new_phase = ph.replace('НОВОЛУНИЕв', 'Новолуние в')
                moon_data.append({'title': new_phase, 'date': date})
    return moon_data


def get_strings_news(data_list):
    acc = []
    for i in data_list:
        acc.append(f"{i['date']}\n{i['title']}")
    acc_string = '\n'.join(acc)
    return acc_string


this_month = scraper(THIS_MONTH)
next_month = scraper(NEXT_MONTH)

phase_text_this_month = get_strings_news(this_month)
phase_text_next_month = get_strings_news(next_month)