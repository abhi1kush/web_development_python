from app import api
from app.api.views import HealthCheckAPIView, RedisDemoAPIView, AddAPIView

api.add_resource(HealthCheckAPIView, '/flask_setup/healthcheck')
api.add_resource(RedisDemoAPIView, '/flask_setup/redis')
api.add_resource(AddAPIView, '/flask_setup/add')
