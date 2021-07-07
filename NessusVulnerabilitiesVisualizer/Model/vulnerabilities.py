class Vulnerabilities:
    def __init__(self, v_id, total_v_nbr, medium_v_nbr, high_v_nbr, critical_v_nbr, ip_id,
                 ip1_id, ip2_id, ip3_id, ip4_id):
        self.v_id = v_id
        self.total_v_nbr = total_v_nbr
        self.medium_v_nbr = medium_v_nbr
        self.high_v_nbr = high_v_nbr
        self.critical_v_nbr = critical_v_nbr
        self.ip_id = ip_id
        self.ip1_id = ip1_id
        self.ip2_id = ip2_id
        self.ip3_id = ip3_id
        self.ip4_id = ip4_id

### TO DO

# def print_vulnerabilities(obj_v):
#     ip_description = getattr(obj_v, "ip_description")
#     ip_1 = getattr(obj_v, "ip_1")
#     ip_2 = getattr(obj_v, "ip_2")
#     ip_3 = getattr(obj_v, "ip_3")
#     ip_4 = getattr(obj_v, "ip_4")
#
#     print("ip = " + str(ip_description))
#     print("ip1 = " + str(ip_1))
#     print("ip2 = " + str(ip_2))
#     print("ip3 = " + str(ip_3))
#     print("ip4 = " + str(ip_4))


def rs_to_vulnerability_obj(result_set):
    v_obj = Vulnerabilities(result_set[0], result_set[1], result_set[2], result_set[3], result_set[4], result_set[5],
                            result_set[6], result_set[7], result_set[8], result_set[9])
    return v_obj
