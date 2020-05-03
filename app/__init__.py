from flask_rq2 import RQ
from flask import Flask
from flask_restful import Api
from app import settings
import rq_dashboard
from flask_swagger_ui import get_swaggerui_blueprint


class BaseRestApiException(Exception):
    pass


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)
    app.name = app.config["APP_NAME"]
    return app


app = create_app()
app.url_map.strict_slashes = False
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/math-ocr/rq")
api = Api(app)
redis_q = RQ(app)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    settings.SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    settings.API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=settings.SWAGGER_URL)

__import__('app.api')

