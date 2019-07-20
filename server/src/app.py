# from flask import Flask

# # app initiliazation
# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     """
#     example endpoint
#     """
#     return {"key": "value"}

# @app.route('/hello', methods=['GET', 'POST'])
# def hello():
#     """
#     example endpoint
#     """
#     return 'Howdy!'

 
# app.run(host='0.0.0.0', port=5000)


from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Top(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {"bye": "baby"}

api.add_resource(Top, '/')


class Task(Resource):
    def get(self):
        """
        Return list of tasks
        """
        return {'hello': 'world'}

    def post(self):
        """
        Create a new task
        """
        hhh = request.form.get("hhh")


        return {"bye": hhh}

api.add_resource(Task, '/task')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
