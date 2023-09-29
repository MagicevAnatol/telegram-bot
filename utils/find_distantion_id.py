import requests
import json
import re
from config_data import config

city_url = 'https://hotels4.p.rapidapi.com/locations/v3/search'
headers = {
    "X-RapidAPI-Key": config.RAPID_API_KEY,
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}


def destination_id(city):
    pattern = '<[^>]*>'
    querystring = {"q":"new york","locale":"en_US","langid":"1033","siteid":"300000001"}
    response = requests.request("GET", city_url, headers=headers, params=querystring)
    data = json.loads(response.text)
    with open('city_dict.json', 'w') as city_file:
        json.dump(data, city_file, indent=4)
    possible_cities = {}
    for i in data['suggestions'][0]['entities']:
        possible_cities[i['destinationId']] = re.sub(pattern, '', i['caption'])
    return possible_cities
