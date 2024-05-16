import sqlite3


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._conn = sqlite3.connect('rental_car.db')
            cls._instance._conn.row_factory = cls._instance.dict_factory
            cls._instance._c = cls._instance._conn.cursor()
        return cls._instance

    @staticmethod
    def dict_factory(cursor, row):
        d = {}
        for index, col in enumerate(cursor.description):
            d[col[0]] = row[index]
        return d

    @property
    def conn(self):
        return self._conn

    @property
    def c(self):
        return self._c

    def close(self):
        self._conn.close()


db = Database()
c = db.c
c.execute('''CREATE TABLE IF NOT EXISTS rental_request (
                       id INTEGER PRIMARY KEY,
                       status TEXT,
                       username TEXT,
                       car_id INTEGER,
                       make TEXT,
                       model TEXT,
                       order_time TEXT,
                       rent_from TEXT,
                       rent_to TEXT,
                       total_price TEXT
                    )''')
conn = db.conn

if __name__ == '__main__':
    from user_manage import UserManage
    UserManage().login_register()
