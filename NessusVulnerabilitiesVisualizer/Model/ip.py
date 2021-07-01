class Ip:
    def __init__(self, ip_id, ip_description, ip_1, ip_2, ip_3, ip_4):
        self.ip_id = ip_id
        self.ip_description = ip_description
        self.ip_1 = ip_1
        self.ip_2 = ip_2
        self.ip_3 = ip_3
        self.ip_4 = ip_4


def print_ip(obj_ip):
    ip_description = getattr(obj_ip, "ip_description")
    ip_1 = getattr(obj_ip, "ip_1")
    ip_2 = getattr(obj_ip, "ip_2")
    ip_3 = getattr(obj_ip, "ip_3")
    ip_4 = getattr(obj_ip, "ip_4")

    print("ip = " + str(ip_description))
    print("ip1 = " + str(ip_1))
    print("ip2 = " + str(ip_2))
    print("ip3 = " + str(ip_3))
    print("ip4 = " + str(ip_4))
