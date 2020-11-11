import datetime
import locale
import calendar
from data_set import days_dict

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

today = datetime.date.today()
days = calendar.monthrange(today.year, today.month)[1]

this_month = datetime.datetime.now()
next_month = this_month + datetime.timedelta(days=days)


def print_result_month(monthes):
    output = []
    for month, value in days_dict.items():
        if month == monthes:
            for date, moon_type in value.items():
                moon = moon_type[0]
                time = moon_type[1]
                output.append(f'{moon} будет {date} в {time}')
    return '\n'.join(output)


THIS_M = print_result_month(this_month.month)
NEXT_M = print_result_month(next_month.month)