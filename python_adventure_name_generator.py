import random

print("Greetings and welcome to the Adventure Name Generator.")
favourite_colour = input("What is your favourite colour?\n")
animal = input("Name an animal:\n")
number = input("Pick a number between 1 and 100:\n")

locations = ["Realm", "Kingdom", "Forest", "Empire", "Valley", "Wasteland", "Isle", "Citadel"]
place = random.choice(locations)

print(f"\nThe name of your adventure is: The {favourite_colour.title()} {animal.title()} of {place}-{number}")
