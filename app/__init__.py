from flask_api import FlaskAPI
# local import
from instance.config import app_config

# initialize sql-alchemy

entries = [{
    'id': 1,
    'title': u'Blockchain',
    'description': u'The chain that has no end',
    'date': '10/10/2018',
    },
    {
    'id': 2,
    'title': u'Schedule',
    'description': u'meet with group members to agree on project delivery',
    'date': '10/10/2018',
    }]

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    return app
