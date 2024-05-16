from utility import print_error, format_date, format_time
from datetime import datetime, timedelta


class BookCar:
    @staticmethod
    def customer_handle():
        from user_manage import UserManage
        from watch_cars import WatchCars
        from review_book import RequestManager
        WatchCars.watch_cars()
        choice = input('1. Book a car 2. Show request 3. back: ')
        if choice == '1':
            BookCar.select_car()
        elif choice == '2':
            RequestManager.print_table('one')
            b = input('Press Enter to back: ')
            if b == '':
                BookCar.customer_handle()

        elif choice == '3':
            UserManage().login_register()

    @staticmethod
    def select_car():
        from main import c
        id = input("Enter the car's ID that you want to rent: ")
        c.execute("SELECT * FROM cars WHERE ID=?", (id,))
        item = c.fetchone()
        if item:
            print(f"You chose: {item['make']} {item['model']} {item['year']}")
        else:
            print_error('Cannot find the car, please check')
            BookCar.select_car()

        days = input("How many days do you want to rent(1-30): ")

        while not days.isdigit() or (int(days) > 30 or int(days) < 1):
            print_error('Invalid input')
            days = input("How many days do you want to rent(1-30): ")
        # while days > 30 OR days < 1:
        insurance = 20
        fee = (item['price'] + insurance) * int(days)
        print(f"The fee is: ({item['price']}$p.d * {days} days) + 20$p.d(insurance) * {days}days = {fee}.00$")
        is_submit = input('1. submit order. 2. back: ')
        while is_submit != '1' and is_submit != '2':
            is_submit = input('1. submit order. 2. back: ')
        if is_submit == '1':
            print('Submit successfully, need to be reviewed by the admin!')
            BookCar.submit_order(item, days, fee)
        elif is_submit == '2':
            BookCar.customer_handle()

    @staticmethod
    def submit_order(item, days, fee):
        from main import c, conn
        from user_manage import UserManage
        now = datetime.now()
        status = 'applying' # applying approved rejected
        order_time = format_time(now)
        rent_from = format_date(datetime.today() + timedelta(days=1))
        rent_to = format_date(datetime.today() + timedelta(days=1+int(days)))
        c.execute('''INSERT INTO rental_request (status, username, car_id, make, model, order_time, rent_from,
            rent_to, total_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (status, UserManage._username,item['id'], item['make'], item['model'], order_time, rent_from, rent_to, fee))
        conn.commit()
        BookCar.customer_handle()


if __name__ == '__main__':
    BookCar.customer_handle()
