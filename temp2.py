
from main import *


c.execute('''CREATE TABLE IF NOT EXISTS cars (
                id INTEGER PRIMARY KEY,
                make TEXT,
                model TEXT,
                year INTEGER,
                mileage REAL,
                available_now INTEGER,
                min_rent_period INTEGER,
                max_rent_period INTEGER
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                car_id INTEGER,
                start_date TEXT,
                end_date TEXT,
                status TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (car_id) REFERENCES cars(id)
             )''')



# Function to register a new user
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (admin/customer): ")

    c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
    conn.commit()
    print("User registered successfully!")



# Function to rent a car
def rent_car(user):
    view_cars()
    car_id = int(input("Enter car ID to rent: "))
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    # Calculate rental fees based on selected car, rental duration, and any additional charges
    # You can implement this calculation based on your business logic

    c.execute("INSERT INTO bookings (user_id, car_id, start_date, end_date, status) VALUES (?, ?, ?, ?, ?)",
              (user[0], car_id, start_date, end_date, "Pending"))
    conn.commit()
    print("Booking request sent!")

# Main function
# Main function
def main():
    logged_in_user = None  # Initialize logged in user as None
    while True:
        print("\nWelcome to Car Rental System")
        print("1. Register")
        print("2. Login")
        print("3. View Available Cars")
        print("4. Rent a Car")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            logged_in_user = login()  # Update logged in user when logged in
        elif choice == '3':
            view_cars()
        elif choice == '4':
            if logged_in_user:  # Check if user is logged in
                rent_car(logged_in_user)
            else:
                print("Please login before renting a car.")
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

