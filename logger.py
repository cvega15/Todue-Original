import time
import os

# finds the location of the executed py file and sets this as the destination for the log.txt
location = os.path.dirname(os.path.abspath(__file__))
def start(file_name):
     # creates the log file and adds the first line
    logger = os.path.join(location, file_name)
    with open(logger, "w+") as handle:
        print(str(time.ctime()) + " >>> Start", file=handle)


def save_create(file_name):
    # creates the save_file at filepath location
    saver = os.path.join(location, file_name)
    with open(saver, "a+"):
        pass
	

def log(message, file_name="log.txt"):
    # appends to log file with specified message
    logger = os.path.join(location, file_name)
    with open(logger, "a") as handle:
        print(str(time.ctime()) + " >>> " + str(message), file=handle)
        

def error(message, file_name):
    # logs a error from python code
    logger = os.path.join(location, file_name)
    with open(logger, "a") as handle:
        print(str(time.ctime()) + " >>> ERROR: " + str(message), file=handle)

'''

Something liek this will go around the main loop in the main file. Then it will run this error! owo
so like try: execpt: finally:

logf = open("download.log", "w")
for download in download_list:
    try:
        # code to process download here
    except Exception as e:     # most generic exception you can catch
        logf.write("Failed to download {0}: {1}\n".format(str(download), str(e)))
        # optional: delete local version of failed download
    finally:
        # optional clean up code
        pass
'''
