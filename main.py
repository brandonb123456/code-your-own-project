import requests
import json

URL = "https://pokeapi.co/"
print(f"Calling{URL}")
response = requests.get(URL)
response.raise_for_status()
data = response.json()
print(f"\nText returned: {response.text}")