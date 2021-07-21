import mariadb
import sys
from NessusVulnerabilitiesVisualizer.Strings import strings


def data_base_connection():
    try:
        connection = mariadb.connect(
            user=strings.USER,
            password=strings.PASSWORD,
            host=strings.HOST,
            port=strings.PORT,
            database=strings.DATABASE
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return connection


def data_base_close_connection_pool(connection):
    print("Disconnedted from " + strings.DATABASE)
    connection.close()


