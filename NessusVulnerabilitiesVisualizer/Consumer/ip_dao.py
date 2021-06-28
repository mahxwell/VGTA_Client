from NessusVulnerabilitiesVisualizer.MariaDB import Db_connection
import mariadb

connection = Db_connection.data_base_connection()


def show_all_ip():
    cursor = connection.cursor()
    try:
        cursor.execute(
            "SELECT * FROM `ip` "
        )
    except mariadb.Error as e:
        print(f"Error: {e}")

    result_set = cursor.fetchall()

    ip_list = []
    for row in result_set:
        ip_list.append(str(row[1]))
    return ip_list
