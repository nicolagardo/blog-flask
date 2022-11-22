#
from flask import Flask

#
from users.routes import user
from blog.routes import blog






def create_app():
    app = Flask(__name__)

    # app.register_blueprint(user)
    app.register_blueprint(blog)

    return app