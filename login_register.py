from watch_cars import watch_cars
from edit_car import handle_car
from utility import print_error
from book_car import customer_handle
from review_book import show_request
_username = ''


def check_username(username):
    from main import c
    c.execute("SELECT * FROM users WHERE username=?", (username, ))

    return c.fetchone()


def register():
    from main import conn, c
    print('--------🍓 be registering--------')
    username = input("Enter username: ")
    # If username is duplicate, let user enter again!
    while check_username(username):
        username = input('Username is duplicate, enter your username: ')
    password = input("Enter password: ")
    input_role = input("Enter role  1.admin 2.customer: ")
    role = ''
    admin = '1'
    customer = '2'
    while admin != input_role != customer:
        print_error('Enter 1 or 2')
        input_role = input("Enter role  1.admin 2.customer: ")
    if input_role == '1':
        role = 'admin'
    elif input_role == '2':
        role = 'customer'

    c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
    conn.commit()
    print("User registered successfully!")
    login_register()


def admin_handle():
    manage = input('1. car list 2. request list 3. customer list: ')
    if manage == '1':
        handle_car()

    elif manage == '2':
        show_request()

def login():
    from main import c
    print('--------🍄 logging --------')
    username = input("Enter username: ")
    password = input("Enter password: ")
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    # print(user['role'])
    if user and user['role'] == 'customer':
        print("Login successful!")
        global _username
        _username = username
        watch_cars()
        customer_handle()
    elif user and user['role'] == 'admin':
        admin_handle()

    else:
        print_error("Invalid username or password!")
        login_register()


def login_register():
    from main import c
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE,
                    password TEXT,
                    role TEXT
                 )''')
    num = int(input('Welcome to car rental system! \n1.login, 2.registration: '))

    if num == 2:
        register()
    elif num == 1:
        login()
    else:
        print_error('Incorrect input! Please re-enter!!')
        login_register()
    

if __name__ == '__main__':
    login_register()
