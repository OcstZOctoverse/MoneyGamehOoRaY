import random

#Variables
money = 0
print("You have " + str(money) + " dollars")
smartness = 0
job = False
house = False
married = False
happiness = 5
prison = False
injury_chance = 0.3
controls = [
  "make money", 
  "get job", 
  "study", 
  "quit", 
  "marry rich", 
  "take drugs", 
  "watch youtube", 
  "brain scan",
  "buy house",
  "meditate",
  "steal",
  "exercise"
]
husbandquality = [
  "the partner is good",
  "the partner is bad"
]
husbandgood = random.choice(husbandquality)
print("Welcome to the game! Your goal is to buy a house")

#Gameplay
while True:

  action = input("What do you want to do? ")
  if action == "get money" or action == "make money" :
    if job is False:
      money += 1
      happiness -= 2
    if job is True:
      money += 5
      happiness -= 2
  if action == "cast spell" or action == "use spell":
    spell = input("What spell do you want to cast? ")
    if spell == "fireball": 
      money -= 5
    if spell == "wish":
      money += 10
  if action == "get job":
    if job = False
      if smartness >= 10:
        print("You got a job!")
        job = True
        happiness += 5
      if smartness < 10:
        print("Too stupid to get a job")
        happiness -= 5
    else:
      print("You already have a job!")
  if action == "study":
    smartness += 1
    happiness -= 0.5
    print("You have " + str(smartness) + " smartness")
  if action == "quit":
    job = False
    happiness += 14
  if action == "marry rich":
    if married is False:
      married = True
      money += 10
      if husbandgood == "the partner is good":
        print("the partner is good")  
        happiness += 7
      if husbandgood == "the partner is bad":
        happiness -= 7
        print("the partner is bad")
    else:
      print("You are already married")
  if action == "brain scan":
    print("smartness: " + str(smartness))
  if action == "watch youtube":
    money -= 1
    happiness += 1.5
    smartness -= 0.5
  if action == "take drugs":
    money -= 8
    smartness -= 5
    happiness += 6
  if action == "meditate":
    money -= 2
    happiness += 5
  if action == "exercise":
    if random.random() <= injury_chance:
      print("You are injured! -7 happiness!")
      happiness -= 7
    else:
      happiness += 2
  if action == "steal":
    if smartness >= 15:
      happiness -= 7
      money += 15
    else:
      prison = True
  if action == "buy house" :
    if money >= 1000:
      house = True
      money -= 1000
      print("You beat the game!")
      break
    else:
      print("You need " + str(1000 - money) + " more dollars to buy a house")
  if action == "help":
    print(" " + str(controls))
  if prison is True:
    happiness -= 10
    money = 0
    print("You are in prison. -10 happiness")
  print("You have " + str(money) + " dollars")
  print("You have " + str(happiness) + " happiness")
  if happiness <= 0:
    print("You died of depression")
    break
  if money < 0:
    print("You are in debt. -3 happiness")
    happiness -= 12
