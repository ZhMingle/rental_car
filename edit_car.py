
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


def del_car(conn, c):
    id = input('Enter the id of the car that you want to delete: ')
    print(id)
    c.execute('DELETE FROM cars WHERE id=?', (id, ))
    conn.commit()

def get_car(conn, c):
    print(1)
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
        print(existing_data)

        # Define the columns of the cars table
        columns = ['make', 'model', 'year', 'mileage', 'available_now', 'min_rent_period', 'max_rent_period', 'price']

        # Display menu for selecting columns to update
        print("Select the columns you want to update:")
        for i, column in enumerate(columns, 1):
            print(f"{i}. {column}")

        selected_columns = input("Enter the column numbers (comma-separated): ")
        selected_columns = selected_columns.split(',')

        # Prompt the user for new values for selected columns
        new_values = []
        for column_index in selected_columns:
            new_value = input(f"Enter the new value for {columns[int(column_index) - 1]}: ")
            new_values.append(new_value)

        # Construct the SQL query
        placeholders = ', '.join([f"{columns[int(column_index) - 1]}=?" for column_index in selected_columns])
        query = f"UPDATE cars SET {placeholders} WHERE id=?"

        # Execute the SQL query
        c.execute(query, new_values + [id_to_update])
        conn.commit()

        print("Car data updated successfully.")
    else:
        print("No car found with the specified ID.")


def handle_car(handle):
    from main import conn, c
    ADD = '1'
    UPDATE = '2'
    DEL = '3'
    if handle == ADD:
        add_car(conn, c)
    elif handle == UPDATE:
        update_car(conn, c)
    elif handle == DEL:
        del_car(conn, c)
