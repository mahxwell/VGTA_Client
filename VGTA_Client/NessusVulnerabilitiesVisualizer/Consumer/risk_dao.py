from NessusVulnerabilitiesVisualizer.MariaDB import Db_connection
import mariadb
from NessusVulnerabilitiesVisualizer.Model import risk

connection = Db_connection.data_base_connection()


def get_risk_from_ip(ip_address):
    cursor_risk = connection.cursor()

    split_ip_address_list = ip_address.split(".")

    # print(split_ip_address_list[0])
    # print(split_ip_address_list[1])
    # print(split_ip_address_list[2])
    # print(split_ip_address_list[3])

    try:
        cursor_risk.execute(
            "SELECT * FROM `risk` WHERE ip_ip1_idip1 = ? AND ip_ip2_idip2 = ? "
            "AND ip_ip3_idip3 = ? AND  ip_ip4_idip4 = ? ", (split_ip_address_list[0], split_ip_address_list[1],
                                                           split_ip_address_list[2], split_ip_address_list[3],)
        )
    except mariadb.Error as e:
        print(f"Error: {e}")

    result_set = cursor_risk.fetchall()
    obj_risk_list = []

    # print(result_set[0][0])
    #
    # i = 0
    # while i < len(result_set):
    #     j = 0
    #     while j < len(result_set[i]):
    #         obj_risk_list.append(risk(result_set[i][j]))
    #         print(obj_risk_list)
    #         j = j + 1
    #     i = i + 1

    return result_set
