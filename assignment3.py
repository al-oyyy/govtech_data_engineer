import requests
import json
import csv
import pandas as pd

url = 'https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json'

#Getting Data from the Given URL
response = requests.get(url)
body_dict = response.json()

#Initialised dictionary with an empty list for each rating name to store the ratings grouped by rating text
ratings = {}
rating_texts = ['Excellent', 'Very Good', 'Good', 'Average', 'Poor']
for text in rating_texts:
    ratings[text] = []

for dict in body_dict:
    for item in dict['restaurants']:
        restaurant = item['restaurant']
        rating = restaurant['user_rating']['rating_text'] #Gets the respective rating level
        rating_score = float(restaurant['user_rating']['aggregate_rating'])
        if rating in rating_texts: #added to exclude other rating_names
            ratings[rating].append(rating_score) #Appends each score in the list for the correct name

for rating_name, rating_list in ratings.items():
    if rating_name == 'Excellent':
        print(rating_name + " boundary: >= " + str(min(rating_list)))
    elif rating_name == 'Poor':
        print(rating_name + " boundary: <= " + str(max(rating_list)))
    else:
        print(rating_name + " boundary: " + str(min(rating_list)) + " - " + str(max(rating_list)))

        
