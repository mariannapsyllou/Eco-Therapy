import unittest
from unittest.mock import MagicMock
from main_OS import EnrollmentGui
import sqlite3
import tkinter as tk


class TestGuiButtonFunction(unittest.TestCase):
    def setUp(self):
        # Set up a test database and table
        self.con = sqlite3.connect(":memory:")
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE users (firstname TEXT, lastname TEXT, email TEXT, birthdate TEXT)")


    def tearDown(self):
        # Clean up the test database and table
        self.cur.execute("DROP TABLE users")
        self.con.close()

    def test_insertion(self):
        self.assertEqual(self.cur.execute("SELECT COUNT(*) FROM users").fetchone()[0], 0)
        first_name_entry = MockEntry("John")
        last_name_entry = MockEntry("Doe")
        email_entry = MockEntry("johndoe@example.com")
        options_year = MockOptionMenu("2021")
        options_month = MockOptionMenu("05")
        options_day = MockOptionMenu("03")

class MockEntry:
    def init(self, text):
        self.text = text

    def get(self):
        return self.text


class MockOptionMenu:
    def init(self, value):
        self.value = value

    def get(self):
        return self.value


if __name__ == "main":
    unittest.main()
