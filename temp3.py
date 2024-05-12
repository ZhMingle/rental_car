class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Car:
    def __init__(self, car_id, make, model, year, mileage, available_now, min_rent_period, max_rent_period):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available_now = available_now
        self.min_rent_period = min_rent_period
        self.max_rent_period = max_rent_period

class Booking:
    def __init__(self, booking_id, user, car, start_date, end_date, status):
        self.booking_id = booking_id
        self.user = user
        self.car = car
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

class CarRentalSystem:
    def __init__(self):
        self.users = []
        self.cars = []
        self.bookings = []

    def register_user(self, username, password, role):
        user = User(username, password, role)
        self.users.append(user)

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def add_car(self, make, model, year, mileage, available_now, min_rent_period, max_rent_period):
        car_id = len(self.cars) + 1
        car = Car(car_id, make, model, year, mileage, available_now, min_rent_period, max_rent_period)
        self.cars.append(car)

    def update_car(self, car_id, make, model, year, mileage, available_now, min_rent_period, max_rent_period):
        for car in self.cars:
            if car.car_id == car_id:
                car.make = make
                car.model = model
                car.year = year
                car.mileage = mileage
                car.available_now = available_now
                car.min_rent_period = min_rent_period
                car.max_rent_period = max_rent_period
                break

    def delete_car(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                self.cars.remove(car)
                break

    def view_available_cars(self):
        available_cars = [car for car in self.cars if car.available_now]
        return available_cars

    # Other methods for managing bookings, calculating rental fees, etc.

# Dummy data for cars
dummy_cars = [
    ('Toyota', 'Corolla', 2018, 50000, 1, 1, 30),
    ('Honda', 'Civic', 2019, 40000, 1, 1, 30),
    ('Ford', 'Fusion', 2017, 60000, 1, 1, 30),
    ('Chevrolet', 'Malibu', 2016, 70000, 1, 1, 30),
    ('Nissan', 'Altima', 2018, 55000, 1, 1, 30),
    ('Hyundai', 'Elantra', 2020, 30000, 1, 1, 30),
    ('Volkswagen', 'Jetta', 2019, 45000, 1, 1, 30),
    ('Kia', 'Optima', 2017, 65000, 1, 1, 30),
    ('BMW', '3 Series', 2018, 50000, 1, 1, 30),
    ('Mercedes-Benz', 'C-Class', 2019, 40000, 1, 1, 30)
]

# Main program
def main():
    car_rental_system = CarRentalSystem()

    # Add dummy cars
    for car_data in dummy_cars:
        car_rental_system.add_car(*car_data)

    while True:
        print("\nWelcome to Car Rental System")
        print("1. Register")
        print("2. Login")
        print("3. View Available Cars")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (admin/customer): ")
            car_rental_system.register_user(username, password, role)
            print("User registered successfully!")
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = car_rental_system.login(username, password)
            if user:
                print("Login successful!")
                if user.role == 'admin':
                    # Implement admin functionalities
                    pass
                else:
                    # Implement customer functionalities
                    pass
            else:
                print("Invalid username or password!")
        elif choice == '3':
            available_cars = car_rental_system.view_available_cars()
            print("Available Cars:")
            for car in available_cars:
                print(f"ID: {car.car_id}, Make: {car.make}, Model: {car.model}, Year: {car.year}, Mileage: {car.mileage}, Min Rent Period: {car.min_rent_period}, Max Rent Period: {car.max_rent_period}")
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
