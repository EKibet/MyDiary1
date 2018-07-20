"""Data retrival and manipulation goes here"""
from flask_restplus import Resource, Namespace, fields, reqparse
from instances.resource import entries_collection, EntryList
from flask import request


''' field attributes goes here'''

entry_namespace = Namespace("User", description="Content related endpoints")
entry_model = entry_namespace.model(
    "content_model", {
        "Description": fields.String(required=True, description="Date vreated"),
        'date_created': fields.DateTime(dt_format='rfc822'),
    })


@entry_namespace.route("/entries")
@entry_namespace.doc(responses={201: "Entry added successfully"})
class EntryMethods(Resource):

    '''Gets all entries'''

    def get(self):

        """Handle get request of url /entries"""

        return entries_collection
    @entry_namespace.expect(entry_model)
    def post(self):
        '''Creates New Entry
        Parses the incoming JSON request data and returns it.'''
        post = request.get_json()
        description = post["Description"]
        date = post['date_created']
        new_entry = EntryList(description,date)
        new_entry.create()
        return {"status_code": "Entry Added successfully"}, 201
