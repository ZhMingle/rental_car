from utility import print_error
from datetime import datetime, timedelta


def customer_handle():
    from login_register import login_register
    from watch_cars import watch_cars
    from review_book import print_table
    watch_cars()
    choice = input('1. Book a car 2. Show request 3. back: ')
    if choice == '1':
        select_car()
    elif choice == '2':
        print_table('one')
        b = input('Press Enter to back: ')
        if b == '':
            customer_handle()

    elif choice == '3':
        login_register()


def select_car():
    from main import c
    id = input("Enter the car's ID that you want to rent: ")
    c.execute("SELECT * FROM cars WHERE ID=?", (id,))
    item = c.fetchone()
    if item:
        print(f"You chosed: {item['make']} {item['model']} {item['year']}")
    else:
        print('Cannot find the car, please check')
        select_car()

    days = input("How many days do you want to rent(1-30): ")

    while not days.isdigit() or (int(days) > 30 or int(days) < 1):
        print_error('Invalid input')
        days = input("How many days do you want to rent(1-30): ")
    # while days > 30 OR days < 1:
    insurance = 20
    fee = (item['price'] + insurance) * int(days)
    print(f"The fee is: ({item['price']}$p.d * {days} days) + 20$p.d(insurance) * {days}days = {fee}.00$")
    is_submit = input('1. submit order. 2. back: ')
    if is_submit == '1':
        print('Submit successfully, need to be reviewed by the admin!')
        submit_order(item, days, fee)
    elif is_submit == '2':
        print('')

def padWith(s):
    return str(s).rjust(2, '0')


def formatTime(time):
    day = padWith(time.day)
    month = padWith(time.month)
    year = time.year
    hour = padWith(time.hour)
    minute = padWith(time.minute)
    second = padWith(time.second)
    return f"{day}/{month}/{year} {hour}:{minute}:{second}"

def formatDate(time):
    day = padWith(time.day)
    month = padWith(time.month)
    year = time.year
    return f"{day}/{month}/{year}"


def submit_order(item, days, fee):
    from main import c, conn
    from login_register import _username
    now = datetime.now()
    status = 'applying' # applying approved rejected
    order_time = formatTime(now)
    rent_from = formatDate(datetime.today() + timedelta(days=1))
    rent_to = formatDate(datetime.today() + timedelta(days=1+int(days)))
    c.execute('''CREATE TABLE IF NOT EXISTS rental_request (
                id INTEGER PRIMARY KEY,
                status TEXT,
                username TEXT,
                car_id INTEGER,
                make TEXT,
                model TEXT,
                order_time TEXT,
                rent_from TEXT,
                rent_to TEXT,
                total_price TEXT
             )''')
    c.execute('''INSERT INTO rental_request (status, username, car_id, make, model, order_time, rent_from,
        rent_to, total_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (status, _username,item['id'], item['make'], item['model'], order_time, rent_from, rent_to, fee))
    conn.commit()


if __name__ == '__main__':
    customer_handle()
