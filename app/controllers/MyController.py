from flask_restful import Resource

class MyController(Resource):
    def get(self):
        return {'message': 'Hello World!'}