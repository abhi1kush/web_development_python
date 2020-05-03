from flask_script import Manager, Shell, Server
from app import app


def _make_context():
    return dict(app=app)


manager = Manager(app)
server = Server(host=app.config["HOST_URL"], port=app.config["HOST_PORT"])
manager.add_command("runserver", server)
manager.add_command("shell", Shell(make_context=_make_context))

if __name__ == "__main__":
    manager.run()

