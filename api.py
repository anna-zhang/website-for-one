import datetime
import requests
from api_key import API_ACCESS_KEY

def get_events(date):
    url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/all/' + date

    headers = {
    'Authorization': API_ACCESS_KEY,
    'User-Agent': 'This Day in History'
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)
    return data