import json
import requests

ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')

ottawa_wards = ottawa_wards_response.json()


for ward in ottawa_wards['objects']:
    print(f"Ward: {ward['name']}")



house_of_commons_response = requests.get('https://represent.opennorth.ca/representatives/house-of-commons/')

house_of_commons = house_of_commons_response.json()

for member in house_of_commons['objects']:
    print(f"First Name: {member['first_name']}\nLast Name: {member['last_name']}\nParty: {member['party_name']}\n")