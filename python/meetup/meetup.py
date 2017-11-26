from datetime import date
from calendar import monthrange
def meetup_day(year, month, day_of_the_week, which):
    print(monthrange(year,month))
    days_of_week = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3, 'Friday':4,'Saturday':5,'Sunday':6}
    for day in days_of_week.keys():
        if day == day_of_the_week:
            day_of_the_week = days_of_week[day]
    if which == 'teenth':
        if date(year,month, 13).weekday() == day_of_the_week:
            return date(year,month,13)
        if date(year,month, 14).weekday() == day_of_the_week:
            return date(year,month,14)
        if date(year,month, 15).weekday() == day_of_the_week:
            return date(year,month,15)
        if date(year,month, 16).weekday() == day_of_the_week:
            return date(year,month,16)
        if date(year,month, 17).weekday() == day_of_the_week:
            return date(year,month,17)
        if date(year,month, 18).weekday() == day_of_the_week:
            return date(year,month,18)
        if date(year,month, 19).weekday() == day_of_the_week:
            return date(year,month,19)
    if which == '1st':
        if date(year,month,1).weekday() == day_of_the_week:
            return date(year,month,1)
        if date(year,month,2).weekday() == day_of_the_week:
            return date(year,month,2)
        if date(year,month,3).weekday() == day_of_the_week:
            return date(year,month,3)
        if date(year,month,4).weekday() == day_of_the_week:
            return date(year,month,4)
        if date(year,month,5).weekday() == day_of_the_week:
            return date(year,month,5)
        if date(year,month,6).weekday() == day_of_the_week:
            return date(year,month,6)
        if date(year,month,7).weekday() == day_of_the_week:
            return date(year,month,7)
    if which == '2nd':
        if date(year,month,8).weekday() == day_of_the_week:
            return date(year,month,8)
        if date(year,month,9).weekday() == day_of_the_week:
            return date(year,month,9)
        if date(year,month,10).weekday() == day_of_the_week:
            return date(year,month,10)
        if date(year,month,11).weekday() == day_of_the_week:
            return date(year,month,11)
        if date(year,month,12).weekday() == day_of_the_week:
            return date(year,month,12)
        if date(year,month,13).weekday() == day_of_the_week:
            return date(year,month,13)
        if date(year,month,14).weekday() == day_of_the_week:
            return date(year,month,14)
    if which == '3rd':
        if date(year,month,15).weekday() == day_of_the_week:
            return date(year,month,15)
        if date(year,month,16).weekday() == day_of_the_week:
            return date(year,month,16)
        if date(year,month,17).weekday() == day_of_the_week:
            return date(year,month,17)
        if date(year,month,18).weekday() == day_of_the_week:
            return date(year,month,18)
        if date(year,month,19).weekday() == day_of_the_week:
            return date(year,month,19)
        if date(year,month,20).weekday() == day_of_the_week:
            return date(year,month,20)
        if date(year,month,21).weekday() == day_of_the_week:
            return date(year,month,21)
    if which == '5th':
        if date(year,month,29).weekday() == day_of_the_week:
            return date(year,month,29)
        if date(year,month,30).weekday() == day_of_the_week:
            return date(year,month,30)
        if date(year,month,31).weekday() == day_of_the_week:
            return date(year,month,31)
    if which == '4th':
        if date(year,month,22).weekday() == day_of_the_week:
            return date(year,month,22)
        if date(year,month,23).weekday() == day_of_the_week:
            return date(year,month,23)
        if date(year,month,24).weekday() == day_of_the_week:
            return date(year,month,24)
        if date(year,month,25).weekday() == day_of_the_week:
            return date(year,month,25)
        if date(year,month,26).weekday() == day_of_the_week:
            return date(year,month,26)
        if date(year,month,27).weekday() == day_of_the_week:
            return date(year,month,27)
        if date(year,month,28).weekday() == day_of_the_week:
            return date(year,month,28)
    if which == 'last' and monthrange(year,month) == (6, 28):
        if date(year,month,22).weekday() == day_of_the_week:
            return date(year,month,22)
        if date(year,month,23).weekday() == day_of_the_week:
            return date(year,month,23)
        if date(year,month,24).weekday() == day_of_the_week:
            return date(year,month,24)
        if date(year,month,25).weekday() == day_of_the_week:
            return date(year,month,25)
        if date(year,month,26).weekday() == day_of_the_week:
            return date(year,month,26)
        if date(year,month,27).weekday() == day_of_the_week:
            return date(year,month,27)
        if date(year,month,28).weekday() == day_of_the_week:
            return date(year,month,28)
    if which == 'last' and monthrange(year,month) == (4, 28):
        if date(year,month,23).weekday() == day_of_the_week:
            return date(year,month,23)
        if date(year,month,24).weekday() == day_of_the_week:
            return date(year,month,24)
        if date(year,month,25).weekday() == day_of_the_week:
            return date(year,month,25)
        if date(year,month,26).weekday() == day_of_the_week:
            return date(year,month,26)
        if date(year,month,27).weekday() == day_of_the_week:
            return date(year,month,27)
        if date(year,month,28).weekday() == day_of_the_week:
            return date(year,month,28)
    if which == 'last':
        if date(year,month,25).weekday() == day_of_the_week:
            return date(year,month,25)
        if date(year,month,26).weekday() == day_of_the_week:
            return date(year,month,26)
        if date(year,month,27).weekday() == day_of_the_week:
            return date(year,month,27)
        if date(year,month,28).weekday() == day_of_the_week:
            return date(year,month,28)
        if date(year,month,29).weekday() == day_of_the_week:
            return date(year,month,29)
        if date(year,month,30).weekday() == day_of_the_week:
            return date(year,month,30)
        if date(year,month,31).weekday() == day_of_the_week:
            return date(year,month,31)



print(meetup_day(2013, 2, 'Saturday', 'last'))
