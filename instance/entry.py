from flask import request, response, Flask
from flask_restful import Namespace, Resource, fields
from instance.entry import DiaryEntry, entries

entries_api = Namespace('random thoughts', description='random thoughts')

random_thoughts = api.model('entry_field', {
    'id': fields.String(required=True, description='Identifier'),
    'description': fields.String(required=True, description='description'),
    'date': fields.fields.String(required=True, description='description'),
})

@api.route('/')
class Entries(Resource):
    @api.doc('list_entries')
    @api.marshal_list_with(entries_api)
    def get(self):
        '''List all entries'''
        return entries
