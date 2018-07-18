#!/usr/bin/python

"""RESTful server implemented using the
Flask-RESTful extension."""

from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path='')
api = Api(app)
auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == 'edgar':
        return 'pygame'
    return None


@auth.error_handler
def unauthorized():

    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog

    return make_response(jsonify({'message': 'Unauthorized access'}),
                         403)

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

entry_fields = {
    'title': fields.String,
    'description': fields.String,
    'done': fields.String,
    'uri': fields.Url('entry'),
    }

'''retrieves a collection of entries.'''
class entryListAPI(Resource):

    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No entry title provided',
                                   location='json')
        self.reqparse.add_argument('description', type=str, default='',
                                   location='json')
        super(entryListAPI, self).__init__()

    def get(self):
        return {'entries': [marshal(entry, entry_fields) for entry in entries]}

    def post(self):
        args = self.reqparse.parse_args()
        entry = {
            'id': entries[-1]['id'] + 1,
            'title': args['title'],
            'description': args['description'],
            'done': False,
            }
        entries.append(entry)
        return ({'entry': marshal(entry, entry_fields)}, 201)
    def post(self):
        args = self.reqparse.parse_args()
        entry = {
            'id': entries[-1]['id'] + 1,
            'title': args['title'],
            'description': args['description'],
            'done': False,
            }
        entries.append(entry)
        return ({'entry': marshal(entry, entry_fields)}, 201)

'''retrieves single entry.'''
class entryAPI(Resource):

    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str,
                                   location='json')
        self.reqparse.add_argument('done', type=str, location='json')
        super(entryAPI, self).__init__()

    def get(self, id):
        entry = [entry for entry in entries if entry['id'] == id]
        if len(entry) == 0:
            abort(404)
        return {'entry': marshal(entry[0], entry_fields)}

    def post(self):
        args = self.reqparse.parse_args()
        entry = {
            'id': entries[-1]['id'] + 1,
            'title': args['title'],
            'description': args['description'],
            'done': False,
            }
        entries.append(entry)
        return ({'entry': marshal(entry, entry_fields)}, 201)

api.add_resource(entryListAPI, '/diary/api/v1.0/entries',
                 endpoint='entries')
api.add_resource(entryAPI, '/diary/api/v1.0/entries/<int:id>',
                 endpoint='entry')

if __name__ == '__main__':
    app.run(debug=True)
