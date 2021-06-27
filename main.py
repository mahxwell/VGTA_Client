from werkzeug.wrappers import Request, Response
from Consumer import ip_dao

# @Request.application
# def application(request):
#     return Response('Hello, World!')


if __name__ == '__main__':
    ip_dao.show_all_ip()

    # Closing connection

    ip_dao.connection.close()


    # from werkzeug.serving import run_simple
    # run_simple('localhost', 4000, application)
