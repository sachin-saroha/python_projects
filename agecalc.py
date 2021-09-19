import datetime
from datetime import timedelta
def ageCalculator(date1):
    today = datetime.datetime.now().date()
    dob = date1
    age = int((today-dob).days / 365.25)
    print("Your age is: ",age)

date_entry = input('Enter a date in DD-MM-YYYY format: ')
day, month, year = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)
ageCalculator(date1)
