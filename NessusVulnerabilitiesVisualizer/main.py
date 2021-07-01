from Consumer import ip_dao
from Webapp import gui_web



if __name__ == '__main__':
    #ip_webapp.launcher()

    from werkzeug.serving import run_simple

    app = gui_web.create_app()
    run_simple("127.0.0.1", 5000, app, use_debugger=True, use_reloader=True)

    # Closing connection

    ip_dao.connection.close()
