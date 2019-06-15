from datetime import datetime

def string_to_datetime(to_convert):

    format = "%Y-%m-%d %H:%M:%S"
    due_date = datetime.strptime(to_convert, format)  

    return due_date
    
