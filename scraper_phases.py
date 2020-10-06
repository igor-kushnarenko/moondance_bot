import requests
from bs4 import BeautifulSoup

URL = 'https://my-calend.ru/moon/2020/october'
HOST = 'https://mirkosmosa.ru/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'user_agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
}


def get_html(url):
    r = requests.get(url)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='moon-date')
    print(items)
    data = []
    for item in items:
        print(item.find('td').get_text('div'))


# def get_text_news_parser(items):
#     acc = []
#     for i in items:
#         acc.append(f"{i['title'].upper()}\n")
#     acc_string = '\n\n'.join(acc)
#     return acc_string


html = get_html(URL)
# print(html.text)
items = get_content(html.text)

