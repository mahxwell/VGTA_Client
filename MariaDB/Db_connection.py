import mariadb
import sys


def data_base_connection():
    try:
        connection = mariadb.connect(
            user="msoro",
            password="toto",
            host="127.0.0.1",
            port=3306,
            database="nessusvulnerabilities"
        )
        print("Connected to " + "nessusvulnerabilities" + " Database with User " + "msoro")

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return connection


def data_base_close_connection_pool(connection):
    connection.close()


