# Budget App

## Outline

- CRUD for monthly bills
- Schedule monthly/weekly payperiod
- Display total of bills due until next pay period

## Steps

1. Create hardcoded bills dictionary
2. Build logic for bi-weekly display
3. Create SQL db connection
4. Build CRUD API
5. Build out front end
6. Build auth

## Logic

- Enter next pay date
- Calculate 2 weeks from that date - 1 day, so 13 days
- Save in local variable
- When today's date == saved dat variable, re-declare date variable

- Grab today's date, sum all dates from today until date variable
