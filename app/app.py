
from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path="")
api = Api(app)
auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == 'edgar':
        return '</>'
    return None


@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)

entries = [
    {
        'id': 1,
        'title': u'Blockchain',
        'description': u'The chain that has no end.',
        'date': '10/1/2018'
    },
    {
        'id': 2,
        'title': u' Schedule',
        'description': u'Meet with the supervisor',
        'date': '10/1/2018'
    }
]

entry_fields = {
    'title': fields.String,
    'description': fields.String,
    'done': fields.String,
    'uri': fields.Url('entry')
}


class Entries_API(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No entry title provided',
                                   location='json')
        self.reqparse.add_argument('description', type=str, default="",
                                   location='json')
        super(Entries_API, self).__init__()

    def get(self):
        return {'entries': [marshal(entry, entry_fields) for entry in entries]}



class EntryAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('date', ype=str, location='json')
        super(entryAPI, self).__init__()

    def get(self, id):
        entry = [entry for entry in entries if entry['id'] == id]
        if len(entry) == 0:
            abort(404)
        return {'entry': marshal(entry[0], entry_fields)}
