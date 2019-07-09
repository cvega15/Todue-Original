from logger import log
from sqlite3 import connect
from uuid import uuid4


class Users(object):

    def __init__(self):

        self.conn = connect('master.db')
        self.curs = self.conn.cursor()

        # creates a table to hold user data if one doesn't exist
        with self.conn:
            self.curs.execute("CREATE TABLE IF NOT EXISTS users(user_id INTIGER, username TEXT, password TEXT, email TEXT, time_created TEXT")

    def check_credentials(self):
        '''
        Checks if password is correct etc. (NOT secure at all though) - TODO NEED GUI
        '''
        return True

    def user_credentials(self): # TODO Encryption
        '''
        bring in input from username and password fields
        '''
        log("Checking User")
        self.current_username = ""                  # INPUT VVVVVV
        self.current_password = ""
        self.current_email = ""
        self.current_user_id = str(uuid4())
