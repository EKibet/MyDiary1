from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class DiaryAPI(Resource):
    def get(self, id):
        pass
    def getOne(self, id):
        pass
    def put(self, id):
        pass
    def post(self, id):
        pass
api.add_resource(DiaryAPI, '/entries', endpoint = 'entry')
