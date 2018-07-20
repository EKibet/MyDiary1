"""Data retrival and manipulation goes here"""
from flask_restplus import Resource, Namespace, fields, reqparse, DateTime, marshal
from instances.resource import entries_collection
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
class UserEntry(Resource):


    '''Gets all entries'''

    def get(self):

        """Handle get request of url /entries"""

        return entries_collection
    @entry_namespace.epect(entry_model)
    def post(self):
        '''Creates New Entry'''
        args = self.reqparse.parse_args()
        entries_collection.append(entry_model)
        return {'entry_model': marshal(entry_model, entry_namespace)}, 201
ffffffffffffffffffffff
ffffffffffff
