from django.http import HttpResponseRedirect
from django.shortcuts import render
from NessusVulnerabilitiesVisualizer.Consumer.ip_dao import *
from NessusVulnerabilitiesVisualizer.Consumer.risk_dao import *
from .models import GetIpAddressForm
from django.urls import reverse


def homepage(request):
    return render(request, "homepage.html")


def search_page(request):
    context = {}
    context['form'] = GetIpAddressForm()
    if request.GET:
        currentip = request.GET['ip_address_field']
        print("current ip search = " + str(currentip))
        # request.session['ip'] = currentip
        # if request.session.has_key('ip'):
        #     ipaddress = request.session['ip']
        #     print(ipaddress)
    return render(request, "search.html", context)


def ip_list(request):
    ip_list = show_all_ip()
    context = {
        "ips": ip_list,
    }
    return render(request, "iplist.html", context)


def ip_vulnerabilities(request, ipaddress):
    # if request.session.has_key('ip'):
    #     ipaddress = request.session['ip']
    current_ip = str(ipaddress)
    obj_risk = get_risk_from_ip(current_ip)

    print(obj_risk)

    print("current ip vuln = " + str(current_ip))
    ip_d = find_id_ip_by_ip_description(current_ip)
    obj_v = find_vulnerabilities_from_ip_address_id(ip_d)
    info = int(getattr(obj_v, "info_v_nbr"))
    low = int(getattr(obj_v, "low_v_nbr"))
    medium = int(getattr(obj_v, "medium_v_nbr"))
    high = int(getattr(obj_v, "high_v_nbr"))
    critical = int(getattr(obj_v, "critical_v_nbr"))

    return render(request, "ip_vulnerabilities.html",  {'obj_v': obj_v, 'obj_risk': obj_risk,
                                                        'labels': ['Info', 'Low', 'Medium', 'High', 'Critical'],
                                                        'data': [info, low, medium, high, critical],
                                                        'colors': ["blue", "green", "yellow", "orange", "red"]})
