from werkzeug.wrappers import Request, Response
from Consumer import ip_dao


@Request.application
def application(request):
    all_ip = ip_dao.show_all_ip()
    for i in range(len(all_ip)):
        print(all_ip[i])
    return Response(all_ip)


def launcher():
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)
