import requests

URL = "https://pokeapi.co/api/v2/pokemon/"
response = requests.get(URL)
response.raise_for_status()
data = response.json()

response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto/")
attributes = response.json()
# print(dir(attributes))
# print(help(attributes))
print(attributes.get("abilities"))

## Andrew will code above this line, Brandon will code below this code ##

print("hello world")