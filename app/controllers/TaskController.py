from flask_restful import Resource
from flask import render_template, make_response, request

class TaskController(Resource):
    def get(self):
        x = request.args.get('x') # Parameter pertama
        y = request.args.get('y') # Parameter kedua
        
        message = "Salah satu parameter tidak diisi, harap isi terlebih dahulu"

        if x and y:
            message = "Kedua paramater telah diisi, nilai tersebut adalah %s, %s" % (x.y)

        view = render_template('task.html', x=x, y=y)
        return make_response(view)