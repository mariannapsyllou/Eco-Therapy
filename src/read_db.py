"""Module for reading database."""
import sqlite3



def read_data() -> list:
    conn = sqlite3.connect('eco-therapy.db')

    cur = conn.cursor()

    cur.execute("""
                SELECT id, name, date, location FROM upcoming_events
                ORDER BY DATE(date) ASC
                LIMIT 3;
                """)

    row = cur.fetchall()
    cur.close()
    conn.close()

    return row


def format_data(data: list):
    id1, name1, when1, where1 = data[0][0], data[0][1], data[0][2], data[0][3]
    id2, name2, when2, where2 = data[1][0], data[1][1], data[1][2], data[1][3]
    id3, name3, when3, where3 = data[2][0], data[2][1], data[2][2], data[2][3]

    return (id1, name1, when1, where1), (id2, name2, when2, where2), (id3, name3, when3, where3)


if __name__ == '__main__':
    read_data()
