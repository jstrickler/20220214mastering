#!/usr/bin/env python
from dateutil import parser
from datetime import datetime, date, timedelta

today = date.today()
print("today:", today)  # <1>
print("type(today): {}".format(type(today)))
print("today.month: {}".format(today.month))
print("today.day: {}".format(today.day))
print("today.year: {}".format(today.year))
print()



now = datetime.now()  # <2>
print("now: {}".format(now))
print("now.day:", now.day)  # <3>
print("now.month:", now.month)
print("now.year:", now.year)
print("now.hour:", now.hour)
print("now.minute:", now.minute)
print("now.second:", now.second)
print("now.microsecond:", now.microsecond)
print()

d1 = datetime(2018, 6, 13, 4, 55, 27, 8082)  # <4>
d2 = datetime(2018, 8, 24)

d3 = d2 - d1  # <5>

print("raw time delta:", d3)
print("time delta days:", d3.days)  # <6>

interval = timedelta(10)  # <7>
print("interval:", interval)

d4 = d2 + interval  # <8>
d5 = d2 - interval
print("d2 + interval:", d4)
print("d2 - interval:", d5)
print()

t1 = datetime(2016, 8, 24, 10, 4, 34)  # <9>
t2 = datetime(2018, 8, 24, 22, 8, 1)
t3 = t2 - t1

print("datetime(2016, 8, 24, 10, 4, 34):", t1)
print("datetime(2018, 8, 24, 22, 8, 1):", t2)
print("time diff (t2 - t1):", t3)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

# def make_date(date_string):
#     year_str, month_str, day_str = date_string.split('-')
#     year = int(year_str)
#     month = int(month_str)
#     day = int(day_str)
#     return date(year, month, day)

for first_name, last_name, product, raw_dob in people:
    # dob = make_date(raw_dob)
    dob = parser.parse(raw_dob)
    print(dob.strftime('%B %d, %Y'))

# 3/2/2022
