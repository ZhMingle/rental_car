from car_manage import CarManage
from utility import print_error, print_success
from book_car import BookCar
from main import c, conn

class UserManage:
    _username = ''

    @staticmethod
    def check_username(username):
        c.execute("SELECT * FROM users WHERE username=?", (username, ))
        return c.fetchone()

    def register(self):
        print('--------🍓 be registering--------')
        input_role = input("Enter role 1.admin 2.customer: ")
        role = ''
        while '1' != input_role != '2':
            print_error('Enter 1 or 2')
            input_role = input("Enter role  1.admin 2.customer: ")
        if input_role == '1':
            role = 'admin'
        elif input_role == '2':
            role = 'customer'
        username = input("Enter username: ")
        # If username is duplicate, let user enter again!
        while self.check_username(username):
            username = input('Username is duplicate, enter your username: ')
        password = input("Enter password: ")

        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
        conn.commit()
        print_success("User registered successfully!")
        self.login_register()

    def admin_handle(self):
        from review_book import RequestManager
        manage = input('1. car list 2. request list: 3. back: ')
        if manage == '1':
            CarManage(conn, c).handle_car()

        elif manage == '2':
            RequestManager().show_request()
        elif manage == '3':
            self.login_register()
        else:
            print_error("Invalid input")
            self.admin_handle()

    def login(self):
        print('--------🍄 logging --------')
        username = input("Enter username: ")
        password = input("Enter password: ")
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        # print(user['role'])
        if user and user['role'] == 'customer':
            print("Login successful!")
            self.__class__._username = username
            BookCar.customer_handle()
        elif user and user['role'] == 'admin':
            self.admin_handle()

        else:
            print_error("Invalid username or password!")
            self.login_register()

    def login_register(self):
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        password TEXT,
                        role TEXT
                     )''')
        num = int(input('Welcome to car rental system! \n1.login, 2.registration: '))

        if num == 2:
            self.register()
        elif num == 1:
            self.login()
        else:
            print_error('Incorrect input! Please re-enter!!')
            self.login_register()

    @property
    def username(self):
        return self._username


if __name__ == '__main__':
    UserManage().login_register()
