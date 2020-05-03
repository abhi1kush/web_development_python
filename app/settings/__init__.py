import os

ENV = os.getenv("ENV", "local")
from .local import *

# if ENV == "production":
#     from .production import *
# elif ENV == "staging":
#     from .staging import *
# else:
#     from .local import *
