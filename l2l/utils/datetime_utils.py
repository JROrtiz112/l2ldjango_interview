from datetime import datetime

def formatDate(dateObject):
    dataType = type(dateObject).__name__
    match dataType:
        case "str":
            # Context give us the iso with a pretty close format "%Y-%m-%dT%H:%M:%S and as a string"
            return dateObject.replace("T", " ")
        case "datetime":
            # Converts the datetime object into a string with a given format
            return dateObject.strftime("%Y-%m-%d %H:%M:%S")
        case _:
            raise TypeError("The data type of the given date is invalid.")