from app import api, web
from app.controllers import MyController, MyViewController

api.add_resource(MyController.MyController, '/')

# Tambahkan route ini
web.add_resource(MyViewController.MyViewController, '/')