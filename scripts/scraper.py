import requests
from bs4 import BeautifulSoup as bs4


# для смены месяцев в адресе нужно заменить названия месяцев
THIS_MONTH = ['https://ru.astro-seek.com/faza-luny-kalendar-lunnyh-faz-onlayn-oktyabr-2020',]
NEXT_MONTH = ['https://ru.astro-seek.com/faza-luny-kalendar-lunnyh-faz-onlayn-noyabr-2020',]

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
                moon_data.append({'title': ph, 'date': date})
            elif 'НОВОЛУНИЕ' in ph:
                moon_data.append({'title': ph, 'date': date})
    return moon_data


def get_strings_news(data_list):
    acc = []
    for i in data_list:
        acc.append(f"{i['date']}\n{i['title']}")
    acc_string = '\n\n'.join(acc)
    return acc_string


this_month = scraper(THIS_MONTH)
next_month = scraper(NEXT_MONTH)

phase_text_this_month = get_strings_news(this_month)
phase_text_next_month = get_strings_news(next_month)
