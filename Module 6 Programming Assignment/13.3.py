from datetime import datetime
with open("today.txt", "r") as file:
    today_string = file.read()
parse = datetime.strptime(today_string, '%m-%d-%Y').date()
