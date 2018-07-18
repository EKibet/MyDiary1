from flask import Flask, jsonify, abort, request, url_for ,make_response
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

entries = [
    {
        'id': 1,
        'title': u'Blockchain',
        'description': u'The chain tha has no end.',
        'date': '10/06/2018'
    },
    {
        'id': 2,
        'title': u'Schedule',
        'description': u'Meet with team members to know how we are progressing',
        'date': '10/06/2018'
    }
]

class EntryListAPI(Resource):
    def get(self, id):
        pass
    def getOne(self, id):
        pass


class EntryAPI(Resource):
    def get(self, id):
        pass
    def put(self, id):
        pass
    def post(self, id):
        pass
api.add_resource(EntryListAPI, '/entries', endpoint = 'entries')
api.add_resource(EntryAPI, '/entries/<int:id>', endpoint = 'entry')
