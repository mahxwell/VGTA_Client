from NessusVulnerabilitiesVisualizer.MariaDB import Db_connection
import mariadb


connection = Db_connection.data_base_connection()


def split_ip_address(ip_address):
    split_ip_address_list = ip_address.split(".")
    return split_ip_address_list


def find_ip_and_ip_range(ip_address):

    list_ip_split = split_ip_address(ip_address)
    print("split ip : " + str(list_ip_split))

    cursor = connection.cursor()
    try:
        cursor.execute(
            "SELECT * FROM `ip` WHERE ip1_idip1 = ? AND ip2_idip2 = ? AND ip3_idip3 =  ? AND ip4_idip4 = ? ",
            (list_ip_split[0],  list_ip_split[1], list_ip_split[2], list_ip_split[3],)
        )
    except mariadb.Error as e:
        print(f"Error: {e}")

    result_set = cursor.fetchall()

    ip_list = []
    for row in result_set:
        ip_list.append(str(row[1]))
    return ip_list


# def get_split_ip_to_table(list_ip_split):
#
#     ip_table = [list_ip_split[0]][list_ip_split[1]][list_ip_split[2]][list_ip_split[3]]
#
#     cursor = connection.cursor()
#
#     for i in len(255):
#         try:
#             cursor.execute(
#                 "SELECT * FROM `ip` WHERE ip1_idip1 = ?",
#                 (list_ip_split[i],)
#             )
#         except mariadb.Error as e:
#             print(f"Error: {e}")
#
#     result_set = cursor.fetchall()
#
#     ip_list = []
#     for row in result_set:
#         ip_list.append(str(row[1]))
#     return ip_list
#
#
# def check_if_star(list_split):
#     for i in range(len(list_split)):
#         if list_split[i] == '*':
#             return True
#     return False
