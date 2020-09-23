import os

ENV = bool(os.environ.get("ENV", True))
if ENV:
    from heroku_config import Var as Config
else:
    from local_config import Development as Config


Var = Config
