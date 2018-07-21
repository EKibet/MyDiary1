"""Data retrival and manipulation goes here"""

from flask_restplus import Resource, Namespace, fields, reqparse
from instances.resource import entries_collection, EntryList
from flask import Flask,request, abort, json

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



''''Get a single/specific entry'''
@entry_namespace.route('/entries/<int:id>')
@entry_namespace.doc(responses = {
        201: "Entry successfully created",
        400: "Invalid parameters provided",
        404: "Entry not found"
        }
        )
class GetOne(Resource):
    def get(self,id):
        single = [entry for entry in entries_collection if entry["id"] == id
        ]
        if len(single) == 0:
            abort(404)
        return single[0]

@entry_namespace.route('/entries/<int:contentID>')
@entry_namespace.doc(
    responses={201: "Entry successfully updated",
        400: "Invalid parameters provided",
        404: "Entry not found"
    })
class UpdateEntry(Resource):
    """Handle PUT request"""

    def get(self, contentID):
        edit = [
            entry for entry in entries_collection
            if entry["id"] == id
        ]
        if len(edit) == 0:
            abort(404)
        return edit

@entry_namespace.expect(entry_model)
def post(self):
    """Handle post request of url/entries"""
    post = request.get_json()
    date = post["Date"]
    entry = post["Content"]
    user_entry = EntryList(date, entry)
    user_entry.create()
    return {"status": "Entry added successfully"}, 201


    def test_api_post_entries(self):
        """Test POST request Method"""
        response = self.client.post(
            '/mydiary/api/v1.0',
            data=json.dumps(self.data),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)
