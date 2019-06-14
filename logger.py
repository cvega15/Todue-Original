import time
import os


location = os.path.dirname(os.path.abspath(__file__))
def start():
    logger = os.path.join(location, "Log.txt")
    with open(logger, "w+") as handle:
        print(str(time.ctime()) + " >>> Start--------------------------------------------------", file=handle)

def log(message):
    # creates log file
    logger = os.path.join(location, "Log.txt")
    with open(logger, "a") as handle:
        print(str(time.ctime()) + " >>> " + str(message), file=handle)



