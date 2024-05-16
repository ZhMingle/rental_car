class WatchCars:
    dummy_cars = [
        ('Toyota', 'Corolla', 2018, 50000, 1, 1, 30, 50),
        ('Honda', 'Civic', 2019, 40000, 1, 1, 30, 60),
        ('Ford', 'Fusion', 2017, 60000, 1, 1, 30, 70),
        ('Chevrolet', 'Malibu', 2016, 70000, 1, 1, 30, 80),
        ('Nissan', 'Altima', 2018, 55000, 1, 1, 30, 90),
        ('Hyundai', 'Elantra', 2020, 30000, 1, 1, 30, 100),
        ('Volkswagen', 'Jetta', 2019, 45000, 1, 1, 30, 110),
        ('Kia', 'Optima', 2017, 65000, 1, 1, 30, 120),
        ('BMW', '3 Series', 2018, 50000, 1, 1, 30, 130),
        ('Mercedes-Benz', 'C-Class', 2019, 40000, 1, 1, 30, 140)
    ]

    @staticmethod
    def is_cars_table_empty():
        from main import c
        c.execute("SELECT COUNT(*) FROM cars")
        count = c.fetchone()['COUNT(*)']
        return count == 0

    # Function to print a row with proper formatting
    @staticmethod
    def print_row(row):
        print("| {:<3} | {:<13} | {:<10} | {:<4} | {:<7} | {:<13} | {:<15} | {:<15} | {:<15} |".format(*row))


    # Function to print the table
    def print_table(data):
        from utility import headers
        signs = "+-----+---------------+------------+------+---------+---------------+-----------------+-----------------+-----------------+"
        # Print header row
        print(signs)
        WatchCars.print_row(headers)
        print(signs)

        # Print data rows
        for row in data:
            WatchCars.print_row(row.values())

        # Print bottom border
        print(signs)

    @staticmethod
    def watch_cars():
        from main import conn, c

        c.execute('''CREATE TABLE IF NOT EXISTS cars (
                    id INTEGER PRIMARY KEY,
                    make TEXT,
                    model TEXT,
                    year INTEGER,
                    mileage REAL,
                    available_now INTEGER,
                    min_rent_period INTEGER,
                    max_rent_period INTEGER,
                    price INTEGER
                 )''')
        if WatchCars.is_cars_table_empty():
            c.executemany("INSERT INTO cars (make, model, year, mileage, available_now, min_rent_period, max_rent_period, "
                          "price) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", WatchCars.dummy_cars)
            conn.commit()
        c.execute("SELECT * FROM cars WHERE available_now=1")
        cars = c.fetchall()

        if cars:
            print("Available Cars:")
            WatchCars.print_table(cars)

        else:
            print("No cars available.")


if __name__ == "__main__":
    WatchCars.watch_cars()