import datetime
now = datetime.datetime.now()
month = now.month
day = now.day
minute = now.minute
second = now.second
print("Current month:", month)
print("Current day:", day)
print("Current minute:", minute)
print("Current second:", second)
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)
def file_operations_demo():
    write_to_file('example.txt', 'Hello, this is a sample text.\n')
    print('File Content:', read_file('example.txt'))
    append_to_file('example.txt', 'Adding more content.\n')
    print('Updated File Content:', read_file('example.txt'))
from datetime import datetime, timedelta
def datetime_demo():
    now = datetime.now()
    print("Current Date and Time:", now)
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Formatted Date and Time:", formatted_now)
    future_date = now + timedelta(days=5)
    print("Future Date (after 5 days):", future_date)
    date1 = datetime(2025, 1, 25)
    date2 = datetime(2025, 2, 1)
    date_diff = date2 - date1
    print("Difference between Dates:", date_diff)
file_operations_demo()
datetime_demo()
