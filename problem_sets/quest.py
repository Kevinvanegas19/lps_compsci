print("Welcome to Kevin's Quest. Your journey starts now")
print("What is your name my fellow human being?")

name = raw_input()

print("Great name dude but before you begin, You're going to choose 3 character attributes.They are going to be strength, health, and luck.  Keep in mind, you have a total of 15 attribute points.")

print("Enter strength,1-10")
strength = int(raw_input())

print("Enter health,1-10")
health = int(raw_input())

print("Enter luck,1-10")
luck = int(raw_input())

if strength + health + luck > 15: 
	strength = int(5)
	health = int(5)
	luck = int(5)
	print("I told you the max was 15. Default attributes have been assigned: strength:5 health:5 luck:5 ")

print("Your name is " + name + ", your strength is " + str(strength) + ", your health is " + str(health) + ", and your luck is " + str(luck))

print(name + ", You've come to a fork in the road. Do you want to go right or left?")
direction = raw_input()
if direction == "right":
	print("Wrong, dead")
else:
	print("Good choice dude")

