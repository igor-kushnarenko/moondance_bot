import datetime
import locale
import calendar

from data_set import days_dict

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def calculate(value, list):
    for date, moon_type in value.items():
        moon = moon_type[0]
        if moon == 'ПОЛНОЛУНИЕ':
            time = moon_type[1]
            list.append(f'🌕 - {date} в {time}')
        elif moon == 'НОВОЛУНИЕ':
            time = moon_type[1]
            list.append(f'🌑 - {date} в {time}')


def print_result_month():
    today = datetime.date.today()
    plus_one_month = calendar.monthrange(today.year, today.month)[1]
    next_month = today + datetime.timedelta(days=plus_one_month)

    this_month_output = []
    next_month_output = []
    for month, value in days_dict.items():
        if month == today.month:
            calculate(value, this_month_output)
        elif month == next_month.month:
            calculate(value, next_month_output)

    this_month_output = '\n'.join(this_month_output)
    next_month_output = '\n'.join(next_month_output)
    return this_month_output, next_month_output


this_month = print_result_month()[0]
next_m = print_result_month()[1]
