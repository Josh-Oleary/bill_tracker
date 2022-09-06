from xml.etree.ElementInclude import include
from data import bills
from datetime import date, timedelta, datetime

today = date.today()
payday = datetime(2022, 9, 8).date()
next_payday = payday + timedelta(days=14)


print(next_payday.day)
print(payday.day)

if payday == date.today():
    payday = today + timedelta(days=14)
elif today > payday:
    payday = payday + timedelta(days=14)

valid_days = [num for num in range(1,32) if num >= today.day and num < payday.day]
next_valid_days = [num for num in range(1,32) if num >= payday.day and num < next_payday.day]
print(next_valid_days)

current_bills = []
next_bills = []


for bill in bills:
    # print(bill)
    if bill in valid_days:
        current_bills.append(bills[bill])
    if bill in next_valid_days:
        next_bills.append(bills[bill])

result = sum(current_bills)
next_result = sum(next_bills)

print(next_bills)

print(f"bills remaining: {result}")
print(f"next bills: {next_result}")
