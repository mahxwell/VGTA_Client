from django.shortcuts import render
from NessusVulnerabilitiesVisualizer.Consumer.ip_dao import show_all_ip


def ip_view(request):
    ip_list = show_all_ip()
    context = {
        "ips": ip_list,
    }
    print(context)
    return render(request, "ip_view.html",  context)
