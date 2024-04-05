from datetime import datetime, timedelta


def get_time(str_time, format_time, time=None):
    if time:
        return datetime.strptime(str_time, format_time).time()
    else:
        return datetime.strptime(str_time, format_time)


def check_date_format(date_string):
    format_string = '%d-%m-%Y %H:%M'
    try:
        datetime.strptime(date_string, format_string)
        return True
    except ValueError:
        return False


def calculate_leave_hours(leave_requests):
    total_leave_hours = 0
    for leave_request in leave_requests:
        if not check_date_format(leave_request['start']) or not check_date_format(leave_request['end']):
            return "Invalid data"
        start_datetime = get_time(leave_request['start'], '%d-%m-%Y %H:%M')
        end_datetime = get_time(leave_request['end'], '%d-%m-%Y %H:%M')
        current_date = start_datetime
        while current_date <= end_datetime:
            start_time = datetime.combine(current_date.date(), get_time("8:30", "%H:%M", True))
            end_time = datetime.combine(current_date.date(), get_time("17:45", "%H:%M", True))
            if start_time.weekday() + 2 not in [7, 8]:
                if start_time <= start_datetime:
                    start_time = start_datetime

                if end_time >= end_datetime:
                    end_time = end_datetime

                if start_time.time() <= get_time("12:00", "%H:%M", True) and end_time.time() >= get_time("13:15",
                                                                                                         "%H:%M", True):
                    leave_hours = (end_time - start_time).total_seconds() / 3600 - 1.25
                else:
                    leave_hours = (end_time - start_time).total_seconds() / 3600

                total_leave_hours += max(leave_hours, 0)
            current_date += timedelta(days=1)

    return total_leave_hours


leave_requests = [
    {"start": "02-01-2024 8:30", "end": "02-01-2024 17:45"},  # 8 tiêngs
    {"start": "08-01-2024 11:30", "end": "09-01-2024 17:45"},  # 13 tiếng
    {"start": "19-01-2024 13:30", "end": "22-01-2024 15:45"},  # 4:25 + 8 + 8 + 6 = 26.25
    {"start": "31-01-2024 8:30", "end": "01-02-2024 14:45"},  # 8 + 5 = 13
]

print(calculate_leave_hours(leave_requests))