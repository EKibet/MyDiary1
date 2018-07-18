from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

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
