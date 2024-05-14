from main import c, conn
from user_manage import UserManage

class RequestManager:
    def __init__(self):
        pass

    def handle_request(self):
        _id = input('Enter the id that you want to handle: ')
        c.execute('SELECT * FROM rental_request WHERE id=?', (_id,))
        one = c.fetchone()
        if not one:
            self.handle_request()
        approve_or_rej = input('1.approve 2.reject: ')
        if approve_or_rej == '1':
            c.execute(f"UPDATE rental_request SET status=? WHERE id=?", ('approve', _id))
            conn.commit()
            self.update_car_status(one['car_id'])
        elif approve_or_rej == '2':
            c.execute(f"UPDATE rental_request SET status=? WHERE id=?", ('reject', _id))
            conn.commit()
        else:
            self.handle_request()

    @staticmethod
    def update_car_status(car_id):
        c.execute(f"UPDATE cars SET available_now=? WHERE id=?", ('0', car_id))
        conn.commit()

    @staticmethod
    def print_table(type='all'):
        if type == 'all':
            c.execute('SELECT * FROM rental_request')
        else:
            c.execute('SELECT * FROM rental_request WHERE username=?', (UserManage._username,))
        data = c.fetchall()
        if not data:
            print("No data available")
            return

        # Get the keys from the first dictionary
        keys = list(data[0].keys())

        # Calculate the maximum width for each column
        column_widths = [max(len(str(row.get(key, ''))) for row in data) for key in keys]

        # Adjust column widths based on header length
        for i, key in enumerate(keys):
            column_widths[i] = max(column_widths[i], len(key))

        # Print table header
        print('+' + '+'.join('-' * (width + 2) for width in column_widths) + '+')
        print('| ' + ' | '.join(key.ljust(width) for key, width in zip(keys, column_widths)) + ' |')
        print('+' + '+'.join('-' * (width + 2) for width in column_widths) + '+')

        # Print table rows
        for row in data:
            print('| ' + ' | '.join(str(row.get(key, '')).ljust(width) for key, width in zip(keys, column_widths)) + '|')

        # Print table footer
        print('+' + '+'.join('-' * (width + 2) for width in column_widths) + '+')

    def show_request(self):
        self.print_table()
        self.handle_request()


if __name__ == '__main__':
    request_manager = RequestManager()
    request_manager.show_request()
