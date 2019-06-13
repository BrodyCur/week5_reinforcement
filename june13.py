import json
import requests

res = requests.get('https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json')
body = json.loads(res.content)

print(body[96].keys())
print(len(body))
print(body[96]['name']) 
print(body[96]['legislatures'][0]['popolo_url']) 

house_res = requests.get('https://cdn.rawgit.com/everypolitician/everypolitician-data/e3ed459db9aea07b357baa6b8edf355bf348a916/data/Japan/House_of_Representatives/ep-popolo-v1.0.json')
house_body = json.loads(house_res.content)

hashimoto = (house_body['persons'][4]['name'])

print(f'Name: {hashimoto}')