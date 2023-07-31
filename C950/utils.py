from datetime import datetime, time

def get_manager_start_time():
  current_date = datetime(1899, 12, 31).date()
  start_time = time(8, 0, 0)

  return datetime.combine(current_date, start_time)

def convert_to_datetime(input):
  return datetime.combine(datetime(1899, 12, 31).date(), time(0, 0, 0)) + input