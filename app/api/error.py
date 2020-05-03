from flask import jsonify, request
from app import app, BaseRestApiException
from app.service_error_codes import ServiceErrorCodes


class BaseAPIException(BaseRestApiException):
    status_code = 400
    message = "Invalid Request"
    service_code = ServiceErrorCodes.BAD_REQUEST_DEFAULT

    def __init__(self, service_code=None, message=None, status_code=None, payload=None):
        Exception.__init__(self)
        if service_code is not None:
            self.service_code = service_code
        if message is not None:
            self.message = message
        elif hasattr(self, "default_message"):
            self.message = self.default_message()
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
        self.success = False

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status'] = self.status_code
        rv['service_code'] = self.service_code
        rv['success'] = self.success
        return rv


class HTTPBadRequest(BaseAPIException):
    status_code = 400
    message = "Bad Request"


class HTTPNotFound(BaseAPIException):
    status_code = 404

    @staticmethod
    def default_message():
        return "Url Not found: {url}".format(url=request.url)


@app.errorhandler(BaseAPIException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(404)
def page_not_found(error):
    return handle_invalid_usage(HTTPNotFound(ServiceErrorCodes.INVALID_URL))