from django.shortcuts import render
from NessusVulnerabilitiesVisualizer.Consumer.ip_dao import show_all_ip
import NessusVulnerabilitiesVisualizer.Model.ip as ip
from django.http import *

IP_LIST = show_all_ip()

def ip_view(request):
   # ip_list = show_all_ip()
    context = {
        "ips": IP_LIST,
    }
    print(context)
    return render(request, "ip_view.html",  context)


def ip_vulnerabilities(request):
    return render(request, "ip_vulnerabilities.html")


def detail_ip(request, ip_list):
    id = int(ip_list) # make sure we have an integer.
    ip_list = IP_LIST[id] # get the album with its id.
    ips = " ".join([ip['ip_description'] for artist in ip_list['ip_descriptions']]) # grab artists name and create a string out of it.
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(ip['ip_descriptions'], ips)
    return HttpResponse(message)
