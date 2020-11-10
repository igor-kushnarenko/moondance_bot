import datetime
import locale
import calendar
from data_set import data_dict, reserv_dict

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

today = datetime.date.today()
days = calendar.monthrange(today.year, today.month)[1]

this_month = datetime.datetime.now()
next_month = this_month + datetime.timedelta(days=days)


def print_result_month(monthes):
    for month, value in reserv_dict.items():
        new_moon = value[0][0]
        new_moon_date = value[0][1]
        new_moon_time = value[0][2]
        full_moon = value[1][0]
        full_moon_date = value[1][1]
        full_moon_time = value[1][2]
        if month == monthes:
            return (f'{new_moon} будет {new_moon_date} в {new_moon_time}\n'
              f'{full_moon} будет {full_moon_date} в {full_moon_time}')


THIS_M = print_result_month(this_month.month)
NEXT_M = print_result_month(next_month.month)