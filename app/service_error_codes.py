class ServiceErrorCodes:
    INVALID_URL = 2001
    METHOD_NOT_ALLOWED = 2050

    BAD_REQUEST_DEFAULT = 2100
    REQUEST_ENTITY_TOO_LARGE = 2120
    KEY_PARSING_ERROR = 2150


CUSTOM_ERROR_MESSAGES = {
    "MethodNotAllowed": {
        "success": False,
        "status": 405,
        "service_code": ServiceErrorCodes.METHOD_NOT_ALLOWED,
        "message": "This metghod is not allowed for the requested resource"
    },
    "RequestEntityTooLarge": {
        "success": False,
        "status": 413,
        "service_code": ServiceErrorCodes.REQUEST_ENTITY_TOO_LARGE,
        "message": "The data transmitted exceed the capacity(32MB) limit."
    }
}