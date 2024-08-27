import requests
import json
import csv
import pandas as pd

url = 'https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json'

#Getting Data from the Given URL
response = requests.get(url)
body_dict = response.json()

#Reading Data from Country Code Excel File
countries = pd.read_excel('Country-Code.xlsx')

#Assigning the name for the eventual csv file and the respective column names
#Open the CSV file used for the final output
file_name = 'restaurants.csv'
columns = ['Restaurant Id', 'Restaurant Name', 'Country', 'City', 'User Rating Votes', 'User Aggregate Rating', 'Cuisines']

with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
    csv_output = csv.DictWriter(csvfile, fieldnames = columns)
    csv_output.writeheader()

    #Iterating through each dictionary in the list
    for dict in body_dict:
        for item in dict['restaurants']:
            restaurant = item['restaurant']
            row = {
                'Restaurant Id': restaurant.get('id','NA'),
                'Restaurant Name': restaurant.get('name','NA'),
                'Country': countries.get(str(restaurant.get('location').get('country_code')).strip(),'NA'),
                'City': restaurant['location'].get('city','NA'),
                'User Rating Votes': restaurant['user_rating'].get('votes','NA'),
                'User Aggregate Rating': float(restaurant['user_rating'].get('aggregate_rating',0.0)),
                'Cuisines':restaurant.get('cuisines','NA')
            }
            csv_output.writerow(row)


print('restaurants.csv is successfully outputted!')




