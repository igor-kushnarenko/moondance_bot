import requests
from bs4 import BeautifulSoup as bs4

URL_LIST = ['https://ru.astro-seek.com/faza-luny-kalendar-lunnyh-faz-onlayn-oktyabr-2020',
            'https://ru.astro-seek.com/faza-luny-kalendar-lunnyh-faz-onlayn-noyabr-2020',
            'https://ru.astro-seek.com/faza-luny-kalendar-lunnyh-faz-onlayn-dekabr-2020'
            ]

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'user_agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
}

full_moon_data = []
empty_moon_data = []

for i in URL_LIST:
    r = requests.get(i).text
    soup = bs4(r, 'lxml')
    block = soup.find('table', style='width: 100%; background: #BBBBBB;')
    phase = block.find_all('tr', class_='ruka')
    for i in phase:
            date = i.find('a').get_text()
            ph = i.find('td', style='padding: 0 5px 0 5px;').get_text()
            if 'Полнолуние' in ph:
                full_moon_data.append({'title': ph, 'date': date})
            elif 'НОВОЛУНИЕ' in ph:
                full_moon_data.append({'title': ph, 'date': date})


def get_strings_news(data_list):
    acc = []
    for i in data_list:
        acc.append(f"{i['date']}\n{i['title']}")
    acc_string = '\n\n'.join(acc)
    return acc_string


phase_text = get_strings_news(full_moon_data)
print(phase_text)
