import yaml
import requests


# Constants
LOCATIONS = 'https://api.domain.com.au/v1/listings/locations'


# Setup
with open('config.yml') as f:
    config = yaml.safe_load(f)
CLIENT_ID = config['CLIENT_ID']
CLIENT_SECRET = config['CLIENT_SECRET']
with open('preferences.yml') as f:
    preferences = yaml.safe_load(f)
print(preferences)


# Get Token
def get_token(client_id, client_secret):
    pass
print(get_token(CLIENT_ID, CLIENT_SECRET))


# Test
def get_locations(search_terms):
    locations = []
    for search_term in search_terms:
        request = requests.get(LOCATIONS, params={'terms':search_term})
        locations.append(request.json())
    return locations
print(get_locations(['2000']))