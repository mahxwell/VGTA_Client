from django.shortcuts import render
from NessusVulnerabilitiesVisualizer.Consumer.ip_dao import *


def homepage(request):
    return render(request, "homepage.html")


def search_page(request):
    return render(request, "search.html")


def ip_list(request):
    ip_list = show_all_ip()
    context = {
        "ips": ip_list,
    }
    return render(request, "iplist.html", context)


def ip_vulnerabilities(request, ipaddress):
    current_ip = str(ipaddress)
    ip_d = find_id_ip_by_ip_description(current_ip)
    obj_v = find_vulnerabilities_from_ip_address_id(ip_d)
    medium = int(getattr(obj_v, "medium_v_nbr"))
    high = int(getattr(obj_v, "high_v_nbr"))
    critical = int(getattr(obj_v, "critical_v_nbr"))
    info = int(getattr(obj_v, "total_v_nbr")) - (medium + high + critical)

    return render(request, "ip_vulnerabilities.html",  {'obj_v': obj_v,
                                                        'labels': ['Medium', 'High', 'Critical', 'Info '],
                                                        'data': [medium, high, critical, info],
                                                        'colors': ["yellow", "orange", "red", "blue"]})