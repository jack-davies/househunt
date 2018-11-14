import yaml
import json
import requests


# Constants
SCOPE = 'api_listings_read'  # requested API
GET_TOKEN = 'https://auth.domain.com.au/v1/connect/token'
GET_LOCATIONS = 'https://api.domain.com.au/v1/listings/locations'
TOKEN_FILE = 'token.json'


# Token functions
def get_token(client_id, client_secret, scope):
    data = {'grant_type':'client_credentials', 'scope':scope}
    request = requests.post(GET_TOKEN, data=data, auth=(client_id, client_secret))
    token = request.json()
    return token

def save_token(token):
    with open(TOKEN_FILE, 'w+') as f:
        json.dump(token, f)

def load_token():
    with open(TOKEN_FILE) as f:
        return json.load(f)


# Setup
with open('config.yml') as f:
    config = yaml.safe_load(f)
CLIENT_ID = config['CLIENT_ID']
CLIENT_SECRET = config['CLIENT_SECRET']
with open('preferences.yml') as f:
    preferences = yaml.safe_load(f)
try:
    token = load_token()
except FileNotFoundError:
    print("Token not found. Requesting new token...")
    token = get_token(CLIENT_ID, CLIENT_SECRET, SCOPE)
    save_token(token)
token_header = {'Authorization':'Bearer ' + token['access_token']}


# Test
def get_locations(search_terms):
    locations = []
    for search_term in search_terms:
        request = requests.get(GET_LOCATIONS, params={'terms':search_term}, headers=token_header)
        locations.append(request.json())
    return locations
print(get_locations(['2000']))