from datetime import datetime
# converts a string into a datetime object and returns that datetime object
def string_to_datetime(to_convert):

    format = "%Y-%m-%d %H:%M:%S"
    due_date = datetime.strptime(to_convert, format)  

    return due_date
    
def datetime_to_mins(to_convert):
    seperated = to_convert.split(" ")
    for item in seperated:
        item = item.split(":")
        print(item)
        


    # return mins
datetime_to_mins("yyyy-mm-dd hh:mm:00")
