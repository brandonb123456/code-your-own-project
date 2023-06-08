import requests

# URL = "https://www.boredapi.com/api/activity/"
#response = requests.get(URL)
#response.raise_for_status()
#data = response.json()
#print ("\nHere are all the kay/value pairs in the JSON response:")
# for key, value in data.items():
#  print (key, ": ", value, sep="")

print("Welcome to the online activity finder!")
print("To find the activity that's just right for you, all you need to do is answer a few simple questions and we'll give you an activity.")
print()
print("Here are the different types of activities.")
print("  1. social")
print("  2. recreational")
print("  3. charity")
print("  4. busywork")
print("  5. diy")
print("  6. cooking")
print("  7. music")
print("  8. education")
print("  9. relaxation")
answer_1 = 0
while answer_1 != "social" or "recreational" or "charity" or "busywork" or "diy" or "cooking" or "music" or "education" or "relaxation":
  answer_1 = str(input("Which type of activity do you prefer?"))
  if answer_1 == "social" or "recreational" or "charity" or "busywork" or "diy" or "cooking" or "music" or "education" or "relaxation":
    break
  else:
    print("Input a valid answer.")
print()
answer_2 = input("How many parcticipants do you want? You can have no more than 4.")
print()
answer_3 = input("What price do you want the activity to be? It can cost 0, but it cannot cost anymore than 0.6.")
print()
answer_4 = input("How accessible do you want the activity to be? 0 is the lowest amount of accessibility, 1 is the highest amount of accessibility.")
print()

type = "/?type=" + str(answer_1)
participants = "#3Dparticipants=" + str(answer_2)
price = "#3Dprice=" + str(answer_3)
accessibility = "#3Daccessibility=" + str(answer_4)

URL = "https://www.boredapi.com/api/activity" + type + participants + price + accessibility
response = requests.get(URL)
response.raise_for_status()
data = response.json()
print (f"Here's an activity for you: {data['activity']}")
  
## Andrew will code above this line, Brandon will code below this code ##

