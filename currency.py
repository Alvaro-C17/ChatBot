import os
import requests
from dotenv import load_dotenv

load_dotenv()

def convert_currency(amount, from_currency, to_currency):
    api_key = os.getenv('OPENEXCHANGE_API_KEY')
    url = f'https://openexchangerates.org/api/convert/{amount}/{from_currency}/{to_currency}?app_id={api_key}'
    response = requests.get(url)
    print(response.status_code)  # Add this line to see the HTTP status code returned by the API
    print(response.json())  # Add this line to see the JSON response returned by the API
    if response.status_code != 200:
        return 'Error: Could not retrieve currency conversion rate'
    data = response.json()
    converted_amount = data['response']
    return converted_amount

