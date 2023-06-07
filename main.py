import requests

URL = "https://pokeapi.co/api/v2/pokemon/"
response = requests.get(URL)
response.raise_for_status()
data = response.json()

## Andrew will code above this line, Brandon will code below this code ##

print("hello world")