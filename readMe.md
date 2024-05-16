## Guidance
1. main.py is the start file
2. open main.py and press start button, or use command line: python ./main.py
3. register first: you can register a customer and a admin
4. login in then just follow the reminder.

## intruduce files

```commandline
- Root
  |-- book_car.py       for customer to select car and book a car 
  |-- car_manage.py     for admin to add, update or delete a car
  |-- main.py           the entry file and create database use singleton pattern
  |-- readMe.md         this
  |-- rental_car.db     database file (start project to create)
  |-- review_book.py    for admin to review the book
  |-- utility.py        some tool functions like formate date and print style
  |-- watch_cars.py     show car list

```
## license: MIT

## Known bugs or issues
1. add a car, don't varify input
2. book a car: Only support whole day and from tomorrow.

