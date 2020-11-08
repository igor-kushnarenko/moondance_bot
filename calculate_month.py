import datetime
import locale
import calendar
from data_set import data_dict

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

today = datetime.date.today()
days = calendar.monthrange(today.year, today.month)[1]

this_month_work = datetime.datetime.now()
next_month_work = this_month_work + datetime.timedelta(days=days)


def print_result_month(monthes):
    for month, value in data_dict.items():
        if month == monthes:
            return value


THIS_M = print_result_month(this_month_work.month)
NEXT_M = print_result_month(next_month_work.month)