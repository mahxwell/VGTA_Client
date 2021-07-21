from NessusVulnerabilitiesVisualizer.MariaDB import Db_connection
from NessusVulnerabilitiesVisualizer.Model import vulnerabilities
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


def find_id_ip_by_ip_description(ip_address):
    if not ip_address:
        return None
    else:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT * FROM `ip` WHERE ip_description = ?",  (ip_address,)
            )
        except mariadb.Error as e:
            print(f"Error: {e}")
    result_set = cursor.fetchall()
    ip_address_id = result_set[0][0]
    return ip_address_id


def find_vulnerabilities_from_ip_address_id(ip_address_id):
    if not ip_address_id:
        return None
    else:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT * FROM `vulnerabilities` WHERE ip_idip = ?", (ip_address_id,)
            )
        except mariadb.Error as e:
            print(f"Error: {e}")
    result_set = cursor.fetchall()
    v_obj = vulnerabilities.rs_to_vulnerability_obj(result_set[0])
    return v_obj
