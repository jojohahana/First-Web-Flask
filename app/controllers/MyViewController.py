from flask_restful import Resource
from flask import render_template, make_response, request

class MyViewController(Resource):
    def get(self):
        view = render_template('index.html')
        return make_response(view)