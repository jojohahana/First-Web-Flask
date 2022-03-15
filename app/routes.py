from app import api, web
from app.controllers import MyController

api.add_resource(MyController.MyController, '/')