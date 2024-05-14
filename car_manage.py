from utility import print_error, print_success, headers
from watch_cars import WatchCars

from abc import ABC, abstractmethod

class AbstractCarManager(ABC):
    def __init__(self, conn, c):
        self.conn = conn
        self.c = c

    @abstractmethod
    def add_car(self):
        pass

    @abstractmethod
    def del_car(self):
        pass

    @abstractmethod
    def update_car(self):
        pass

class CarManage(AbstractCarManager):
    def __init__(self, conn, c):
        super().__init__(conn, c)
        self.conn = conn
        self.c = c

    def add_car(self):
        make = input("Enter the car's make: ")
        model = input("Enter the car's model: ")
        year = input("Enter the car's year: ")
        mileage = input("Enter the car's mileage: ")
        available_now = 1
        min_rent_period = 1
        max_rent_period = 30
        price = input("Enter the car's price: ")
        self.c.execute('''INSERT INTO cars (make, model, year, mileage,available_now, min_rent_period, max_rent_period, price) VALUES 
        (?, ?, ?, ?, ?, ?, ?, ?)''', (make, model, year, mileage, available_now, min_rent_period, max_rent_period, price))
        self.conn.commit()
        print_success('Add car successfully')
        self.handle_car()

    def del_car(self):
        id = input('Enter the id of the car that you want to delete: ')
        self.c.execute('SELECT * FROM cars WHERE id=?', (id,))
        item = self.c.fetchall()
        if item:
            WatchCars.print_table(item)
            make_sure = input(f'Confirm delete the car: 1.yes 2.no: ')
            if make_sure == '1':
                self.c.execute('DELETE FROM cars WHERE id=?', (id,))
                self.conn.commit()
        else:
            print_error('The ID you input is not exist')
        self.handle_car()

    def update_car(self):
        id_to_update = input("Enter the ID of the car you want to update: ")
        self.c.execute('SELECT * FROM cars WHERE id=?', (id_to_update,))
        existing_data = self.c.fetchone()

        if existing_data:
            print("Existing data:")
            WatchCars.print_table([existing_data])

            print("Select the columns you want to update:")
            for i, header in enumerate(headers[1:], 1):
                print(f"{i}. {header}")

            selected_columns = input("Enter the headers numbers (comma-separated): ")
            selected_columns = selected_columns.split(',')

            new_values = []
            for column_index in selected_columns:
                new_value = input(f"Enter the new value for {headers[int(column_index)]}: ")
                new_values.append(new_value)

            placeholders = ', '.join([f"{headers[int(column_index)]}=?" for column_index in selected_columns])
            query = f"UPDATE cars SET {placeholders} WHERE id=?"

            self.c.execute(query, new_values + [id_to_update])
            self.conn.commit()

            print_success("Car data updated successfully.")
        else:
            print_error("No car found with the specified ID.")
        self.handle_car()

    def handle_car(self):
        WatchCars.watch_cars()
        handle = input('1. add car 2. update car 3. delete car 4. back: ')
        while handle not in ['1', '2', '3', '4']:
            handle = input('1. add car 2. update car 3. delete car 4. back: ')
        if handle == '1':
            self.add_car()
        elif handle == '2':
            self.update_car()
        elif handle == '3':
            self.del_car()
        elif handle == '4':
            UserManage.admin_handle()
        else:
            self.handle_car()


if __name__ == '__main__':
    from main import conn, c
    from user_manage import UserManage
    car_manager = CarManage(conn, c)
    car_manager.handle_car()
