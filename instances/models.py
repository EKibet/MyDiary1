"""Data retrival and manipulation goes here"""

from flask_restplus import Resource, Namespace, fields, reqparse
from instances.resources import entries_collection, EntryList
from flask import Flask

''' field attributes goes here'''

entry_namespace = Namespace("User", description="Content related endpoints")
entry_model = entry_namespace.model(
    "content_model", {
        "id":fields.String(required=True, description="Identifier"),
        "Description": fields.String(required=True, description="Description"),
        'date_created': fields.DateTime(dt_format='rfc822'),
    })

@entry_namespace.route("/entries")
@entry_namespace.doc(responses={201: "Entry added successfully"})
class EntryMethods(Resource):

    '''Gets all entries'''

    def get(self):
        """Handle get request of url /entries"""
        return entries_collection
