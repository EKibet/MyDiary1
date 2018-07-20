from flask import Flask
from flask_restplus import Api
from app.config import app_config
api = Api(
    version="1.0",
    title ="MyDiary API endpoints",
    description="Endpoints to retrieve,add and modify entries in MyDiary",
    prefix="/mydiary/api/v1.0"
)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    from instances.models import entry_namespace as entries
    api.add_namespace(entries, path="/user")
    api.init_app(app)
    return app
