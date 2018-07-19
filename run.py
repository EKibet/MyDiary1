#!flask/bin/python

"""RESTful server implemented using the
Flask-RESTful extension."""

from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_httpauth import HTTPBasicAuth
from app.app import *

api.add_resource(Entries_API, '/diary/api/v1.0/entries', endpoint='entries')
api.add_resource(EntryAPI, '/diary/api/v1.0/entries/<int:id>', endpoint='entry')


if __name__ == '__main__':
    app.run(debug=True)
