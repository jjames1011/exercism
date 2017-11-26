from datetime import date
def meetup_day(year, month, day_of_the_week, which):
    days_of_week = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3, 'Friday':4,'Saturday':5,'Sunday':6}
    for day in days_of_week.keys():
        if day == day_of_the_week:
            day_of_the_week = days_of_week[day]

    if date(year,month, 13).weekday() == day_of_the_week:
        return date(year,month,13)
    
print(meetup_day(2013, 5, 'Monday', 'teenth'))
