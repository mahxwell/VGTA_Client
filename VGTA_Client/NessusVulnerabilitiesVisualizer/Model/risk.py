class Risk:
    def __init__(self, risk_id, risk_description, severity, solutions, cve, ip_id, ip_1, ip_2, ip_3, ip_4):
        self.risk_id = risk_id
        self.risk_description = risk_description
        self.severity = severity
        self.solutions = solutions
        self.cve = cve
        self.ip_id = ip_id
        self.ip_1 = ip_1
        self.ip_2 = ip_2
        self.ip_3 = ip_3
        self.ip_4 = ip_4


def print_risk(obj_risk):
    risk_description = getattr(obj_risk, "risk_description")
    severity = getattr(obj_risk, "severity")
    solutions = getattr(obj_risk, "solutions")
    cve = getattr(obj_risk, "cve")
    ip_id = getattr(obj_risk, "ip_id")
    ip_1 = getattr(obj_risk,"ip_1")
    ip_2 = getattr(obj_risk, "ip_2")
    ip_3 = getattr(obj_risk, "ip_3")
    ip_4 = getattr(obj_risk, "ip_4")

    print("risk description = " + str(risk_description))
    print("severity = " + str(severity))
    print("solutions = " + str(solutions))
    print("cve = " + str(cve))
    print("ip id = " + str(ip_id))
    print("ip1 = " + str(ip_1))
    print("ip2 = " + str(ip_2))
    print("ip3 = " + str(ip_3))
    print("ip4 = " + str(ip_4))


def rs_to_risk_obj(result_set):
    risk = Risk(result_set[0], result_set[1], result_set[2], result_set[3],
                result_set[4], result_set[5], result_set[6], result_set[7],
                result_set[8], result_set[9])
    return risk
