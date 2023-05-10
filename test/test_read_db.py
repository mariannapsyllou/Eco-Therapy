import unittest
from unittest import TestCase, mock
from src.read_db import DbInteraction

class TestDbInteraction(TestCase):

    @mock.patch('src.read_db.sqlite3')
    def test_read_data(self, mock_sqlite3):
        # set up the mock cursor and connection
        mock_cursor = mock_sqlite3.connect.return_value.cursor.return_value
        mock_cursor.fetchall.return_value = [(1, 'event1', '2023-05-08', 'location1'),
                                              (2, 'event2', '2023-05-09', 'location2'),
                                              (3, 'event3', '2023-05-10', 'location3')]
        # create an instance of the class and call the method
        db_interaction = DbInteraction()
        result = db_interaction.read_data()
        # check that the expected data was returned
        expected_result = ((1, 'event1', '2023-05-08', 'location1'),
                           (2, 'event2', '2023-05-09', 'location2'),
                           (3, 'event3', '2023-05-10', 'location3'))
        
        self.assertEqual(result, expected_result)
        # check that the expected database query was executed
        mock_cursor.execute.assert_called_once_with("SELECT id, name, date, location FROM upcoming_events ORDER BY DATE(date) ASC LIMIT 3")

    @mock.patch('src.read_db.sqlite3')
    def test_write_db(self, mock_sqlite3):
        # set up the mock cursor and connection
        mock_cursor = mock_sqlite3.connect.return_value.cursor.return_value
        mock_cursor.lastrowid = 1
        # create an instance of the class and call the method
        db_interaction = DbInteraction()
        db_interaction.write_db('John', 'Doe', 'johndoe@example.com', '1990-01-01', 1)
        # check that the expected data was written to the database
        mock_cursor.execute.assert_has_calls([mock.call("""INSERT INTO users (firstname, lastname, email, birthdate) VALUES (?, ?, ?, ?)""", ('John', 'Doe', 'johndoe@example.com', '1990-01-01')),
        mock.call("""INSERT INTO enrolled (user_id, event_id) VALUES (?, ?)""", (1, 1))])
        mock_cursor.lastrowid = 2
        db_interaction.write_db('Jane', 'Doe', 'janedoe@example.com', '1995-01-01', 2)
        mock_cursor.execute.assert_has_calls([mock.call("""INSERT INTO users (firstname, lastname, email, birthdate) VALUES (?, ?, ?, ?)""", ('Jane', 'Doe', 'janedoe@example.com', '1995-01-01')),
        mock.call("""INSERT INTO enrolled (user_id, event_id) VALUES (?, ?)""", (2, 2))])

    def test_format_data(self):
        # set up input and expected output
        input_data = [(1, 'event1', '2023-05-08', 'location1'),
                      (2, 'event2', '2023-05-09', 'location2'),
                      (3, 'event3', '2023-05-10', 'location3')]
        expected_output = ((1, 'event1', '2023-05-08', 'location1'),
                           (2, 'event2', '2023-05-09', 'location2'),
                           (3, 'event3', '2023-05-10', 'location3'))

        # create an instance of the class and call the method
        db_interaction = DbInteraction()
        result = db_interaction.format_data(input_data)

        # check that the expected output was returned
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()