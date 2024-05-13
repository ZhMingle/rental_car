from utility import print_error, print_success, headers
from watch_cars import print_table
def add_car(conn, c):
    make = input("Enter the car's make: ")
    model = input("Enter the car's model: ")
    year = input("Enter the car's year: ")
    mileage = input("Enter the car's mileage: ")
    available_now = 1
    min_rent_period = 1
    max_rent_period = 30
    price = input("Enter the car's price: ")
    c.execute('''INSERT INTO cars (make, model, year, mileage,available_now, min_rent_period, max_rent_period, price) VALUES 
    (?, ?, ?, ?, ?, ?, ?, ?)''', (make, model, year, mileage, available_now, min_rent_period, max_rent_period, price))
    conn.commit()
    print_success('Add car successfully')
    handle_car()

def del_car(conn, c):
    id = input('Enter the id of the car that you want to delete: ')
    c.execute('SELECT * FROM cars WHERE id=?', (id,))
    item = c.fetchall()
    if item:
        print_table(item)
        make_sure = input(f'Confirm delete the car: 1.yes 2.no: ')
        if make_sure == '1':
            c.execute('DELETE FROM cars WHERE id=?', (id,))
            conn.commit()
    else:
        print_error('The ID you input is not exist')
    handle_car()

def update_car(conn, c):
    # id = input('Enter the id of the car that you want to update: ')
    # c.execute("SELECT * FROM users WHERE id=?", (id, ))

    # Prompt the user for input
    id_to_update = input("Enter the ID of the car you want to update: ")

    # Fetch the existing data
    c.execute('SELECT * FROM cars WHERE id=?', (id_to_update,))
    existing_data = c.fetchone()

    if existing_data:
        print("Existing data:")
        print_table([existing_data])

        # Display menu for selecting columns to update
        print("Select the columns you want to update:")
        for i, header in enumerate(headers[1:], 1):
            print(f"{i}. {header}")

        selected_columns = input("Enter the headers numbers (comma-separated): ")
        selected_columns = selected_columns.split(',')

        # Prompt the user for new values for selected columns
        new_values = []
        for column_index in selected_columns:
            new_value = input(f"Enter the new value for {headers[int(column_index)]}: ")
            new_values.append(new_value)

        # Construct the SQL query
        placeholders = ', '.join([f"{headers[int(column_index)]}=?" for column_index in selected_columns])
        query = f"UPDATE cars SET {placeholders} WHERE id=?"

        # Execute the SQL query
        c.execute(query, new_values + [id_to_update])
        conn.commit()

        print_success("Car data updated successfully.")
    else:
        print("No car found with the specified ID.")
    handle_car()


def handle_car():
    from main import conn, c
    from login_register import admin_handle
    from watch_cars import watch_cars
    watch_cars()
    handle = input('1. add car 2. update car 3. delete car 4. back: ')
    ADD = '1'
    UPDATE = '2'
    DEL = '3'
    BACK = '4'
    if handle == ADD:
        add_car(conn, c)
    elif handle == UPDATE:
        update_car(conn, c)
    elif handle == DEL:
        del_car(conn, c)
    elif handle == BACK:
        admin_handle()


if __name__ == '__main__':
    handle_car()
