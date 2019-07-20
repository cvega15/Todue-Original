'''
install pip
install git
install postgres
pip install psycopg

-------


CREATE TABLE tasks(user_id INTEGER, task_id SERIAL, task_name TEXT, time_due TEXT, time_made TEXT, notifications TEXT, PRIMARY KEY(task_id));

CREATE TABLE users(user_id SERIAL, email TEXT, username TEXT, PRIMARY KEY(user_id));
ALTER TABLE users ADD CONSTRAINT unique_username UNIQUE(username);

'''

import psycopg2
# must create this with vars using the format below
from dbconfig import postgresdatabase, postgrespassword, postgresusername

# Try to connect

try:
    conn = psycopg2.connect(host = "localhost", dbname=dbconfig.postgresdatabase, user=dbconfig.postgresusername, password=dbconfig.postgrespassword) # ALTER USER postgres PASSWORD 'pswchange';
except:
    print("I am unable to connect to the database.")
    exit()
    
curs = conn.cursor()  

try:
    cur.execute("SELECT * from users")
except:
    print("I can't SELECT from users")

rows = curs.fetchall()
for row in rows:
    print("   ", row)