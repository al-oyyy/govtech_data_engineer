import requests
import json
import csv
import pandas as pd
from datetime import datetime

url = 'https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json'

#Getting Data from the Given URL
response = requests.get(url)
body_dict = response.json()

file_name = 'restaurant_events.csv'
columns = ['Event Id', 'Restaurant Id', 'Restaurant Name', 'Photo URL', 'Event Title', 'Event Start Date', 'Event End Date']

#Function that will check if the string date of an event is in the designated period of April 2019
def date_checker(event_date_string):
    event_date = datetime.strptime(event_date_string, '%Y-%m-%d')
    if event_date.month == 4 and event_date.year == 2019:
        return True
    else:
        return False
    
with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
    csv_output = csv.DictWriter(csvfile, fieldnames = columns)
    csv_output.writeheader()

    #Iterating through each dictionary in the list
    for dict in body_dict:
        for item in dict['restaurants']:
            restaurant = item['restaurant']
            restaurant_id = restaurant['id']
            restaurant_name = restaurant['name']

            #We will sieve through the restaurant's zomato events
            for event_row in restaurant.get('zomato_events',[]):
                event = event_row['event']
                start_date = event['start_date']
                end_date = event['end_date']
                if date_checker(start_date) or date_checker(end_date):
                    pass
                else:
                    row = {
                        'Event Id': event['event_id'],
                        'Restaurant Id': restaurant_id,
                        'Restaurant Name': restaurant_name,
                        'Photo URL':event['photos'][0]['photo']['url'] if event['photos'] else 'NA',
                        'Event Title': event['title'],
                        'Event Start Date': start_date,
                        'Event End Date': end_date
                    }
                    csv_output.writerow(row)

print('restaurant_events.csv created successfully!')
