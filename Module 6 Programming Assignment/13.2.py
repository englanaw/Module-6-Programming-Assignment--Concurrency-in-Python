from datetime import date 

with open('today.txt', 'r') as file:
    today_string = file.read()

    print (today_string)