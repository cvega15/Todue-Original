import time
import os


location = os.path.dirname(os.path.abspath(__file__))

def log(message):
    # creates log file
    logger = os.path.join(location, "Log.hdf")
    with open(logger, "w+") as handle:
        print(str(time.ctime()) + " >>> " + str(message), file=handle)
