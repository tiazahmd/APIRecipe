'''
Category Based Recipe App Version 1.0
You choose a category and have the option to do the following on those categories:
1. See a list of 10 recipes based on that category
2. Generate a random recipe from that category

Code: Imtiaz Ahmed
'''

# import and open files
import requests
import json
import random
nameFile = open('name.txt', 'w')
ingredientsFile = open('ingredients.txt', 'w')
instructionsFile = open('instructions.txt', 'w')
# end import and opened files


# create database based on category

foodCategory = ["chicken", "shrimp", "pasta", "burger", "cocktails"]

print("-----------------------------------------------------------")
print("--------------Welcome to the Random Recipe App-------------")
print("-----------------------------------------------------------")
print("Choose a category: ")
print("1. Chicken")
print("2. Shrimp")
print("3. Pasta")
print("4. Burger")
print("5. Cocktails")
print("-----------------------------------------------------------")

# category selection & validation
userCatChoice = -1
while userCatChoice < 0 or userCatChoice > 4:
    try:
        userCatChoice = (int(input("Enter your choice (1-5): "))) - 1
    except ValueError:
        print("Please only enter integers")
    if userCatChoice < 0 or userCatChoice > 4:
        print("Wrong choice. Please enter a choice between 1-5")
print("-----------------------------------------------------------")
print("Connecting to api...")
# end category selection & validation

# setting app key & id parameters
parameters = {"app_id": "ccb957ea", "app_key": "86f66ada97edeb480e0112b7e3e355fd", "q": foodCategory[userCatChoice]}

# establishing connection
response = requests.get('https://api.edamam.com/search', params = parameters)

# checking if API is working okay
if response.status_code == 200:
    print("Connection established to API. Database updated")
    print("-----------------------------------------------------------")
else:
    print("API Conection Failed")
# end checking if API is working okay

# updating the database
data = response.json()
for i in range(0,10):
    nameFile.write(data["hits"][i]["recipe"]["label"] + '\n')
    ingrLen = len(data["hits"][i]["recipe"]["ingredientLines"])
    ingredientsFile.write("Ingredients: You'll need " + str(ingrLen) + " ingredients.\n")
    instructionsFile.write("Instructions: " + data["hits"][i]["recipe"]["url"] + '\n')

nameFile.close()
ingredientsFile.close()
instructionsFile.close()
# end updating the database
# end create database based on categories

# begin main program
userChoice = 0

while userChoice != 3:

    print("----------------------Menu---------------------------------")
    print("1. See list of recipes")
    print("2. Generate a random recipe")
    print("3. Quit")
    # user input & validation
    try:
        userChoice = int(input("Select an option (1-3): "))
    except ValueError:
        print("Please only enter integers")
    if userChoice < 1 or userChoice > 3:
        print("Wrong choice. Please select an option between 1 and 3")
    print("-----------------------------------------------------------")
    # end user input and validation

    # user wants to see the list of recipes
    if userChoice == 1:
        with open('name.txt') as nameFile:
            for i in range(0,10):
                print(str(i+1) + ". " + str(nameFile.readline()))
    # end user wants to see the list of recipes

    # user wants to generate a random recipe
    if userChoice == 2:
        randNum = random.randint(0,9)

        nameFile = open('name.txt')
        nameLine = nameFile.read().splitlines()
        print("Name: " + nameLine[randNum])

        ingredientsFile = open('ingredients.txt')
        ingredientLines = ingredientsFile.read().splitlines()
        print(ingredientLines[randNum])

        instructionsFile = open('instructions.txt')
        instructionLine = instructionsFile.read().splitlines()
        print(instructionLine[randNum])

        nameFile.close()
        ingredientsFile.close()
        instructionsFile.close()
    # end user wants to generate a random recipe

# end main program
