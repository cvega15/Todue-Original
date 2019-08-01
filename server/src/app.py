from flask import Flask, request
from flask_restful import Resource, Api
import dbconnect
import json
# must have dbconfig file
from dbconfig import postgresdatabase, postgrespassword, postgresusername

def convert(tup, di): 
    di = dict(tup) 
    return di 

app = Flask(__name__)
api = Api(app)

class Task(Resource):
    """
    Return Info about one task
    """
    def get(self, task_id):
        conn = psycopg2.connect(host = "localhost", dbname=dbconfig.tasksdatabase, user=dbconfig.postgresusername, password=dbconfig.postgrespassword) # ALTER USER postgres PASSWORD 'pswchange';
        curs = conn.cursor()
        cur.execute("SELECT * from users where task_id = %s" % task_id)
        rows = curs.fetchall()
        return json.dumps(convert(rows, {}))

    def post(self, task_id):
        x = 'JSON TEXT INPUT'
        xjson = json.loads(x) # for every post

        conn = psycopg2.connect(host = "localhost", dbname=dbconfig.tasksdatabase, user=dbconfig.postgresusername, password=dbconfig.postgrespassword) # ALTER USER postgres PASSWORD 'pswchange';
        curs = conn.cursor()
        cur.execute("") # TODO: NEW INPUT HERE from variable (EDIT METHOD)
        # might need return??

api.add_resource(Task, '/user/' + user_id + task_id + '/') - # TODO: Make sure people cant edit the url to see someone else's task (check id's before display)


class TodoList(Resource):
    """
    Return list of tasks for one user
    """
    def get(self, user_id):
        conn = psycopg2.connect(host = "localhost", dbname=dbconfig.tasksdatabase, user=dbconfig.postgresusername, password=dbconfig.postgrespassword) # ALTER USER postgres PASSWORD 'pswchange';
        curs = conn.cursor()
        cur.execute("SELECT * from users where user_id = %s" % user_id)
        rows = curs.fetchall()
        return json.dumps(convert(rows, {}))


    def post(self, user_id):
        conn = psycopg2.connect(host = "localhost", dbname=dbconfig.tasksdatabase, user=dbconfig.postgresusername, password=dbconfig.postgrespassword) # ALTER USER postgres PASSWORD 'pswchange';
        curs = conn.cursor()
        cur.execute("SELECT * from users where user_id = %s" % user_id)
        rows = curs.fetchall()
        for row in rows:
            return row


api.add_resource(Task, '/user/' + user_id + '/') # TODO: How to set user_id

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