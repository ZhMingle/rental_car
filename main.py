import sqlite3
from login_register import login_register
from edit_car import update_car


def dict_factory(cursor, row):
    d = {}
    for index, col in enumerate(cursor.description):
        d[col[0]] = row[index]
    return d


conn = sqlite3.connect('rental_car.db')
conn.row_factory = dict_factory
c = conn.cursor()

if __name__ == '__main__':
    login_register()
    # update_car(conn, c)



# def updateCar(carList):
#     carList[0]['year'] = 2016
