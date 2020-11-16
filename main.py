"""
MadLibs
Author: Evan Wilson
Period/Core: 6


"""
#mad libs story genorator
story = int(input("pick either story number \n 1 \n 2 \n "))


#story 1
if story == 1:
  print("This is a preview of the mad lib")

  print("____ went to Thanksgiving at _____. ____ ate old ____ and expired _____. ")

  print("During Thanksgiving, __________ marshmallow yams played in the TV while we were talking about who is the __________ out of all of us. The ____ was dancing up a storm while the rest of us were ______ dancing ")

  print("Before we left, we had to ____ wioth everyone about who is the __________. ____ was the one that was picked and ____ was ____.")

  name = input("Enter a name: ")
  adjective1 = input("Enter an adjective: ")
  adjective2 = input("Enter an adjective: ")
  adverb = input("Enter an adverb: ")
  food1 = input("Enter a food: ")
  food2 = input("Enter another food: ")
  noun = input("Enter a noun: ")
  place = input("Enter a place: ")
  verb = input("Enter a verb: ")
  mood = input("Are you happy or sad? ")
  
  print(f"{name} went to Thanksgiving at {place}. {name} ate old {food1} and expired {food2}. ")

  print(f"During Thanksgiving, {adjective1} marshmallow yams played in the TV while we were talking about who is the {adjective2} out of all of us. The {noun} was dancing up a storm while the rest of us were {adverb} dancing ")

  print(f"Before we left, we had to {verb} wioth everyone about who is the {adjective2}. {name} was the one that was picked and {name} was {mood}.")


#story 2
else:

  print("This is a preview of the mad lib")

  print("_____ went on a walk with _____. They were talking about _____ food that they had eaten over at _____.")

  name1 = input("Enter a name: ")
  name2 = input("Enter another name: ")
  name3 = input("Enter another another name: ")
  gross = input("pick either garbage or stinky: ")

  print(f"{name1} went on a walk with {name2}. They were talking about {gross} food that they had eaten over at {name3}.")