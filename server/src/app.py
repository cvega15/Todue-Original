from flask import Flask, request
from flask_restful import Resource, Api
import dbconnect

app = Flask(__name__)
api = Api(app)

class Task(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {"bye": "baby"}

api.add_resource(Task, '/user/' + user_id + '/task_id') - # TODO: Make sure people cant edit the url to see someone else's task (check id's before display)


class TodoList(Resource):
    pass

api.add_resource(Task, '/user/' + user_id)

class UserList(Resource):
    def get(self):
        """
        Return list of users from db -- RESTRICTED
        """
        self.todo_list = dbconnect.db_retrieve_all("userdatabase")

api.add_resource(UserList, '/users/all/')

class AllTasks(Resource):
    def get(self):
        """
        Return list of tasks from db -- RESTRICTED
        """
        self.todo_list = dbconnect.db_retrieve_all("tasksdatabase")

api.add_resource(AllTasks, '/tasks/all/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)