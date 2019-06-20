from datetime import datetime
# cnoverts a date_time object into a readable format for calculating time_delta (see classes.py > Timer) 
def datetime_to_string(to_convert):
    seperated = to_convert.split(" ")
    date = seperated[0].split("-")
    time = seperated[1].split(":")
    seperated = date + time
    return seperated
    # should return [yyyy, mm, dd, H, M, S]

def datetime_to_string_for_save(to_convert):
    return datetime.strftime(to_convert, "%Y-%m-%d %H:%M:%S")