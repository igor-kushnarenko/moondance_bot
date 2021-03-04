import datetime
import locale
import calendar

from data_set import days_dict

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

today = datetime.date.today()
plus_one_day = datetime.datetime.today() + datetime.timedelta(days=1)

tomorrow = plus_one_day.strftime('%d %B')
plus_one_month = calendar.monthrange(today.year, today.month)[1]

next_month = today + datetime.timedelta(days=plus_one_month)


def send_alert():
    for month, value in days_dict.items():
        for date, moon_type in value.items():
            if tomorrow == date:
                moon = moon_type[0]
                time = moon_type[1]
                send_alert_message = f'Завтра в {time} будет {moon}!'
                return send_alert_message


def print_result_month(months):
    output = []
    for month, value in days_dict.items():
        if month == months:
            for date, moon_type in value.items():
                moon = moon_type[0]
                if moon == 'ПОЛНОЛУНИЕ':
                    time = moon_type[1]
                    output.append(f'🌕 - {date} в {time}')
                elif moon == 'НОВОЛУНИЕ':
                    time = moon_type[1]
                    output.append(f'🌑 - {date} в {time}')
    str_output = '\n'.join(output)
    return str_output


THIS_M = print_result_month(today.month)
NEXT_M = print_result_month(next_month.month)

SEND_ALERT = send_alert()
