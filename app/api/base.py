from flask import request, jsonify
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from app.api.error import HTTPBadRequest
from app.service_error_codes import ServiceErrorCodes


class BaseAPIResource(Resource):
    error = ""

    def dispatch_request(self, *args, **kwargs):
        validate_func = getattr(self, f'test_{request.method.lower()}', None)
        try:
            is_validate_failed = validate_func and not validate_func(*args, **kwargs)
        except BadRequest as e:
            if e and hasattr(e, 'data'):
                raise HTTPBadRequest(
                    service_code=e.data.get(
                        'service_code', ServiceErrorCodes.KEY_PARSING_ERROR),
                    message=e.data.get('message')
                )
            raise HTTPBadRequest
        if is_validate_failed:
            message = getattr(self, 'error', '')
            if message:
                raise HTTPBadRequest(message=message)
            raise HTTPBadRequest
        data = super(BaseAPIResource, self).dispatch_request(*args, **kwargs)
        if data.get("success") is None:
            data["success"] = True
        return jsonify(data)
