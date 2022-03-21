from app import api, web
from app.controllers.MyViewController import MyViewController
from app.controllers import MyController, MyViewController, TaskController

api.add_resource(MyController.MyController, '/')

# Tambahkan route ini
web.add_resource(MyViewController.MyViewController, '/')
web.add_resource(MyViewController.MySecondViewController, '/say-my-name')
web.add_resource(TaskController.TaskController, '/dua-parameter')