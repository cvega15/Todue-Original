#!/usr/bin/env python3
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import socket
import psycopg2
import json
from google.oauth2 import id_token
from google.auth.transport import requests as requests_google
import requests

print('starting server')

#initialize app
app = Flask(__name__)
CORS(app)

#functions for database access
def get_connection(): 
    return psycopg2.connect(host = "localhost", dbname="todo_app", user="postgres", password="postgres")

def add_task_db(curs, task, user_id): 
    curs.execute("INSERT INTO tasks (task_name, due_time, notifications, task_id, last_updated, user_id, time_made) VALUES(%s, %s, %s, %s, %s, %s, %s)",
    (task.get('task_name'), task.get('due_time'), task.get('notifications'), task.get('task_id'), task.get('last_updated'), user_id, task.get('time_made'))) 

def delete_task_db(curs, data, user_id):
    curs.execute("DELETE FROM tasks WHERE task_id = %s AND user_id = %s", (data, user_id))       

#function for authorizing token with each request
def authorize_token(token): 
    try:  
        decoded_token = id_token.verify_oauth2_token(token, requests_google.Request(), "195081855240-jjsqpn2t0oucb8ets7li98p8vodja8jd.apps.googleusercontent.com")   
        print(decoded_token) 
        if(decoded_token.get('aud') == "195081855240-jjsqpn2t0oucb8ets7li98p8vodja8jd.apps.googleusercontent.com" and decoded_token.get('iss') == "accounts.google.com"): 
            print('epicsauce') 
            return decoded_token 
        else:
            return False
    except:
        return False

#functions for requests
@app.route('/sign-up-in', methods=['POST'])
def sign_up_in():
    print('sign up in ') 
    conn = get_connection()
    curs = conn.cursor()   
    data = (request.get_data(as_text = False)).decode('utf-8')
    payload = {'code': data, 'client_id':'195081855240-jjsqpn2t0oucb8ets7li98p8vodja8jd.apps.googleusercontent.com', 'client_secret': 'BRxJqpHe3J8ct7czwuca_jXg', 'grant_type': 'authorization_code', 'redirect_uri': 'postmessage', 'access_type':'offline'} 

    try:
        resp = json.loads((requests.post('https://oauth2.googleapis.com/token', params=payload)).text)
        id_token = authorize_token(resp.get('id_token')) 
        user_id = id_token.get('sub')
        curs.execute("SELECT user_id FROM users") 
        le_data = (curs.fetchall())
        le_data = [user_id[0] for user_id in le_data]
        settings = '{"clock_mode":false}'

        if(user_id not in le_data):
            print('creating user account')
            curs.execute("INSERT INTO users (name, user_id, email, settings) VALUES(%s, %s, %s, %s)", (id_token.get('given_name'), id_token.get('sub'), id_token.get('email'), settings)) 

        else:
            print('user already has account, logging in') 
            print('token authorized, user logged in, returning refresh token, id_token and access token')
        
        conn.commit()
        curs.close()
        conn.close() 
        return jsonify(resp)
        
    except:
        return jsonify(resp)

@app.route('/post-settings', methods=['POST'])
def post_settings():
    print('posting settings') 
    data = request.get_data() 
    data = str((data.decode("utf-8")).strip("''"))
    decoded_token = authorize_token(request.headers['Authorization'])

    if(decoded_token != False):
        conn = get_connection()
        curs = conn.cursor()

        curs.execute("UPDATE users SET settings = %s WHERE user_id = %s", (data, decoded_token.get('sub'))) 

        conn.commit()
        curs.close()
        conn.close()
        return str(data)
    else:
        print('error')
        return  jsonify({"result" : "failure", "error" : "401", "message" : "was not able to authorize user"}), 401

@app.route('/get-settings', methods=['GET'])
def get_settings():
    print('get settings') 
    token = authorize_token(request.headers['Authorization'])

    if(token != False):
        conn = get_connection()
        curs = conn.cursor()
        
        curs.execute("SELECT settings FROM users WHERE user_id = %s", [token.get('sub')])
        settings = curs.fetchone()[0] 

        curs.close()
        conn.close()
        return jsonify(settings) 
    
    else:
        print('error')
        return  jsonify({"result" : "failure", "error" : "401", "message" : "was not able to authorize user"}), 401

@app.route('/recieve-all-tasks', methods=['POST'])
def recieve_all_tasks():   
    print('recieving all tasks') 
    data = request.get_json()
    token = authorize_token(request.headers['Authorization'])

    if(token != False):
        conn = get_connection() 
        curs = conn.cursor()     
        
        for task in data:
            print(task)
            add_task_db(curs, task, token.get('sub')) 

        conn.commit()
        curs.close()
        conn.close()
        return str(data)
    
    else:
        print('error')
        return  jsonify({"result" : "failure", "error" : "401", "message" : "was not able to authorize user"}), 401

@app.route('/get-tasks', methods=['GET'])
def get_tasks():        
    print('getting tasks')
    token = authorize_token(request.headers['Authorization']) 

    if(token != False):
        conn = get_connection()
        curs = conn.cursor() 
        curs.execute("SELECT row_to_json(tasks) FROM tasks WHERE user_id = %s", [token.get('sub')]) 

        rows = (curs.fetchall()) 
        rows = [row[0] for row in rows]  

        curs.close() 
        conn.close()
        return jsonify(rows)
    
    else:
        print('error')
        return  jsonify({"result" : "failure", "error" : "401", "message" : "was not able to authorize user"}), 401

@app.route('/delete-task', methods=['DELETE'])
def delete_task():
    print('deleting task')
    token = authorize_token(request.headers['Authorization'])
    
    if(token != False):
        data = str(request.get_json()) 
        conn = get_connection()
        curs = conn.cursor() 
        
        delete_task_db(curs, data, token.get('sub'))

        conn.commit()
        curs.close()
        conn.close()
        return str(data)
    
    else:
        print('error')
        return jsonify({"result" : "failure", "error" : "401", "message" : "was not able to authorize user"}), 401

@app.route('/post-task', methods=['POST'])
def post_task():
    print('posting task')
    token = authorize_token(request.headers['Authorization'])

    if(token != False):
        data = request.get_json()
        conn = get_connection()
        curs = conn.cursor()
    
        add_task_db(curs, data, token.get('sub'))

        conn.commit()
        curs.close()
        conn.close() 
        return str(data)

    else:
        print('error')
        return jsonify({"result" : "failure", "error" : "401", "message" : "was not able to authorize user"}), 401

@app.route('/edit-task', methods=['POST'])
def edit_task():
    print('editing task')
    token = authorize_token(request.headers['Authorization'])
    
    if(token != False):
        data = request.get_json()
        conn = get_connection()
        curs = conn.cursor()

        user_id = token.get('sub')
        delete_task_db(curs, data.get('task_id'), user_id)
        add_task_db(curs, data, user_id) 

        conn.commit()
        curs.close()
        conn.close()
        return str(data)

    else:
        print('error')
        return jsonify({"result" : "failure", "error" : "401", "message" : "was not able to authorize user"}), 401

@app.route('/recieve-ticket', methods=['POST'])
def recieve_ticket():
    print('recieving ticket') 
    decoded_token = authorize_token(request.headers['Authorization'])

    if(decoded_token != False):    
        data = request.get_json() 
        conn = get_connection()
        curs = conn.cursor()
        user_id = decoded_token.get('sub')        

        for action in data:
            action_mode = action.get('mode');   
            task = action.get('data'); 

            if action_mode == 'add':
                add_task_db(curs, task, user_id) 
               
            elif action_mode == 'edit': 
                curs.execute('SELECT last_updated FROM tasks WHERE task_id = %s AND user_id = %s', (task.get('task_id'), user_id))

                last_updated = (curs.fetchone())[0]
                
                if(task.get('last_updated') > int(last_updated)):
                    delete_task_db(curs, task.get('task_id'), user_id) 
                    add_task_db(curs, task, user_id) 

            elif action_mode == 'delete':
                delete_task_db(curs, task, user_id)

        conn.commit()
        curs.close()
        conn.close()
        return str(data)

    else:
        print('error')
        return jsonify({"result" : "failure", "error" : "401", "message" : "was not able to authorize user"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug='False')




