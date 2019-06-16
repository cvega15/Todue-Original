import time
import os

# finds the location of the executed py file and sets this as the destination for the Log.txt
location = os.path.dirname(os.path.abspath(__file__))
def start():
     # creates the log file and adds the first line
    logger = os.path.join(location, "log.txt")
    with open(logger, "w+") as handle:
        print(str(time.ctime()) + " >>> Start", file=handle)

def log(message):
    # appends to log file
    logger = os.path.join(location, "log.txt")
    with open(logger, "a") as handle:
        print(str(time.ctime()) + " >>> " + str(message), file=handle)



        
