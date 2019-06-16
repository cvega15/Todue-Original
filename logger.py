import time
import os


location = os.path.dirname(os.path.abspath(__file__))
def start():
     # creates the log file and adds the first line --  if file exists, it overrides what is in it
    logger = os.path.join(location, "Log.txt")
    with open(logger, "w+") as handle:
        print(str(time.ctime()) + " >>> Start", file=handle)

def log(message):
    # appends to log file
    logger = os.path.join(location, "Log.txt")
    with open(logger, "a") as handle:
        print(str(time.ctime()) + " >>> " + str(message), file=handle)



        
