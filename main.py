import requests
import json

URL = "https://pokeapi.co/"
print(f"Calling{URL}")
response = requests.get(URL)
response.raise_for_status()
data = response.json()
print(f"\nText returned: {response.text}")

## Andrew will code above this line, Brandon will code below this code ##

print("hello world")