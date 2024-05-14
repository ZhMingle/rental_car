
# Define cars headers
headers = ['ID', 'Make', 'Model', 'Year', 'Mileage', 'Available Now', 'Min Rent Period', 'Max Rent Period', 'Price']


def print_error(text='error'):
    print(f"\033[31m{text}\033[0m")


def print_success(text='error'):
    print(f"\033[32m{text}\033[0m")


def pad_with(s):
    return str(s).rjust(2, '0')


def format_time(time):
    day = pad_with(time.day)
    month = pad_with(time.month)
    year = time.year
    hour = pad_with(time.hour)
    minute = pad_with(time.minute)
    second = pad_with(time.second)
    return f"{day}/{month}/{year} {hour}:{minute}:{second}"


def format_date(time):
    day = pad_with(time.day)
    month = pad_with(time.month)
    year = time.year
    return f"{day}/{month}/{year}"