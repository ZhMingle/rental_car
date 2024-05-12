# import mysql.connector
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root"
#     ,
#     password="Zml890098@"
# )
#
# mycursor = mydb.cursor()
# mycursor.execute('USE DATABASE myDatabase1')
# admin.py

class Admin:
    def __init__(self, event_dispatcher):
        self.event_dispatcher = event_dispatcher

    def create_user(self, username, password):
        # Logic to create a new user
        self.event_dispatcher.dispatch("user_created", username)


# user.py
class User:
    def __init__(self, event_dispatcher):
        self.event_dispatcher = event_dispatcher

    def on_user_created(self, username):
        print(f"New user created: {username}")


# event_dispatcher.py
class EventDispatcher:
    def __init__(self):
        self.listeners = {}

    def add_listener(self, event_name, listener):
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(listener)

    def dispatch(self, event_name, *args, **kwargs):
        if event_name in self.listeners:
            for listener in self.listeners[event_name]:
                listener(*args, **kwargs)

def main():
    event_dispatcher = EventDispatcher()

    admin = Admin(event_dispatcher)
    user = User(event_dispatcher)

    event_dispatcher.add_listener("user_created", user.on_user_created)

    # Example usage
    admin.create_user("john_doe", "password123")


if __name__ == "__main__":
    main()

# mycursor.execute("CREATE TABLE Customers(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),address VARCHAR(255))")
#
# sql = "INSERT INTO Customers (name,address) VALUES (%s,%s)"
# val = ("zml", "69 Symonds St")
# mycursor.execute(sql, val)