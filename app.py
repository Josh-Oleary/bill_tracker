from xml.etree.ElementInclude import include
from data import bills
from datetime import date, timedelta, datetime

today = date.today()
payday = datetime(2022, 9, 8).date()

if payday == date.today():
    payday = today + timedelta(days=14)
elif today > payday:
    payday = payday + timedelta(days=14)

valid_days = [num for num in range(1,32) if num >= today.day and num < payday.day]

current_bills = []

for bill in bills:
    # print(bill)
    if bill in valid_days:
        current_bills.append(bills[bill])

print(current_bills)

result = sum(current_bills)

print(f"bills remaining: {result}")