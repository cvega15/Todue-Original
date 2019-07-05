import logger
import sqlite3
import uuid


class Users(object):

    def __init__(self):

        self.conn = sqlite3.connect('master.db')
        self.curs = self.conn.cursor()

        # creates a table to hold user data if one doesn't exist
        with self.conn:
            self.curs.execute("CREATE TABLE IF NOT EXISTS users(user_id TEXT, username TEXT, password TEXT, time_made TEXT)")
    
    def check_credentials(self):
        '''
        Checks if password is correct etc. (NOT secure at all though) - TODO NEED GUI
        '''
        return True
    def user_credentials(self): # TODO Encryption
        '''
        bring in input from username and password fields
        '''
        logger.log("Checking User")
        self.current_username = ""                  # INPUT VVVVVV
        self.current_password = ""
        self.current_email = ""
        self.current_user_id = str(uuid.uuid4())
