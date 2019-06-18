import time
import os

# finds the location of the executed py file and sets this as the destination for the log.txt
location = os.path.dirname(os.path.abspath(__file__))
def start():
     # creates the log file and adds the first line
    logger = os.path.join(location, "log.txt")
    with open(logger, "w+") as handle:
        print(str(time.ctime()) + " >>> Start", file=handle)
    # creates the save_file at filepath location
    saver = os.path.join(location, "save_files.txt")
    with open(saver, "a+"):
        pass
	

def log(message):
    # appends to log file with specified message
    logger = os.path.join(location, "log.txt")
    with open(logger, "a") as handle:
        print(str(time.ctime()) + " >>> " + str(message), file=handle)
        
