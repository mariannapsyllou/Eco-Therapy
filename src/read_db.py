"""Module for reading database."""
import sqlite3


class DbInteraction:
    """
    A class that interacts with a SQLite database named 'eco-therapy.db'.
    It contains methods to read data from and write data to the database.

    Methods:
    --------
    __init__():
        Initializes the object by creating a connection to the database.

    read_data():
        Reads data from the 'upcoming_events' table of the database.
        Returns the data as a tuple of three tuples containing id, name, date,
        and location of the events.

    format_data(data: list):
        Formats the data returned by the 'read_data' method into a tuple of
        three tuples.

    write_db(first_name: str, last_name: str, email: str, birthday: str, Eid:
    int):
        Writes user data and the event id to the 'users' and 'enrolled' tables
        of the database, respectively.
    """
    def __init__(self):
        self.connection = sqlite3.connect('eco-therapy.db')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def read_data(self):
        """Reads 3 upcoming events from database and returns id, name, date,
        location"""
        # Dont change this line to fit line-length, will mess with unittest
        self.cursor.execute("""SELECT id, name, date, location FROM upcoming_events ORDER BY DATE(date) ASC LIMIT 3""")
        data = self.cursor.fetchall()
        return self.format_data(data)

    def format_data(self, data: list):
        """Formats data that hase been read from database"""
        formatted_data = []
        for row in data:
            event_id, name, date, location = row
            formatted_data.append((event_id, name, date, location))
        return tuple(formatted_data)

    def write_db(self, first_name, last_name, email, birthday, event_id):
        """Writes users data to database"""
        with self.connection:
            self.cursor.execute("""
                INSERT INTO users (firstname, lastname, email, birthdate)
                VALUES (?, ?, ?, ?)
            """, (first_name, last_name, email, birthday))
            user_id = self.cursor.lastrowid

            self.cursor.execute("""
                INSERT INTO enrolled (user_id, event_id)
                VALUES (?, ?)
            """, (user_id, event_id))
