from datetime import datetime
# converts a string into a datetime object and returns that datetime object (see main > adding task/changing due date)
def string_to_datetime(to_convert):

    format = "%Y-%m-%d %H:%M:%S"
    due_date = datetime.strptime(to_convert, format)  

    return due_date

# cnoverts a date_time object into a readable format for calculating time_delta (see classes.py > Timer) 
def datetime_to_string(to_convert):
    seperated = to_convert.split(" ")
    date = seperated[0].split("-")
    time = seperated[1].split(":")
    seperated = date + time
    return seperated
    # should return [yyyy, mm, dd, H, M, S]

def date_to_minutes(to_convert):
    # converts a datetime string (see above) into minutes
    return (to_convert[3] * 60 + to_convert[4] + to_convert[5] // 60)