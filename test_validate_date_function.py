from datetime import datetime

def validate_date(data, previous_date):
    try:
        input_date = datetime.strptime(data["DATE"], "%m/%d")
        start_date = datetime.strptime(data["DATE_RANGES"]["start_date"], "%m-%d-%Y")
        end_date = datetime.strptime(data["DATE_RANGES"]["end_date"], "%m-%d-%Y")


        if start_date <= input_date <= end_date:
            if previous_date:
                previous_date_obj = datetime.strptime(previous_date, "%Y-%m-%d")
                if previous_date_obj <= input_date:
                    return input_date.strftime("%Y-%m-%d")
                else:
                    raise Exception("Invalid previous date")
            else:
                return input_date.strftime("%Y-%m-%d")
        else:
            raise Exception( "Date out of specified range")
    except ValueError:
        raise Exception("Invalid date format")

