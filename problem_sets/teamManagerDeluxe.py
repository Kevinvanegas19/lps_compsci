# makes our class
class Player(object):
	#object which has their name, age, goals, jersey number, and position 
        def __init__(self, name, age, goals, jersey_number, position):
		self.name  = name
		self.age = age
		self.goals = goals
		self.jersey_number = jersey_number
		self.position = position
	#summary of stats
	def getPlayerSummary(self):
		print("Name:" + self.name)
		print("Age:" + self.age)
		print("Goals:"+ self.goals)
		print("Jersey Number:" + self.jersey_number)
		print("Position:" + self.position)
		
# make function that saves the team
def saveTeam(myPlayers, filename):
	#open file
	my_file = open(filename, "a")
	for lol in myPlayers:
		#write in file
		my_file.write(lol.name + " " + str(lol.age) + " " + str(lol.goals) + " " + str(lol.jersey_number) + " " + lol.position + "\n")
	# close the file
	my_file.close()
	 
# make a function to load the team 
def loadTeam(filename):
	empty_list = []
	# open file
	my_file = open(filename, "r")
	# read line or file
	waldo = my_file.readline()
	while waldo != "":
		# split to be a list
		myWords = waldo.split()
		# add to list 
		empty_list.append(Player(str(waldo[0]), str(waldo[1]), str(waldo[2]), str(waldo[3]), str(waldo[4]) + "\n")) 
		waldo = my_file.readline()
	# close the file
	my_file.close()
	return empty_list

print("Welcome to Team Manager Deluxe!")
print("Do you want to start a new team or open an existing team?")
print("Enter the # of your choice")
print("(1) Start with a new team")
print("(2) Open a file for an existing team")
choice = raw_input()

# if their choice is 2, then we should load the file team
if choice == "2":
	# ask what the name of the file is
	print("What's the filename for your existing team? Enter the whole name with the .tmd exetension")
	# allow them to input it
	filename = raw_input()
	myPlayers = loadTeam(filename)
# else if they choose 1, start with a new team
else:
	myPlayers = []

print("What do you want to do? Enter the # and press Enter.")
print("(1) Add a player")
print("(2) Print all players")
print("(3) Save your player list to a file")
print("(0) Leave the program (save first to avoid losing your data!)")
choice = raw_input()

lul = True
# if choice is 1, add a player
while lul:
	if choice == "1":
		print("Enter name:")
		nombre = raw_input()
		print("Enter age:")
		edad = raw_input()
		print("Enter goals:")
		goals = raw_input()
		print("Enter jersey number:")
		jerseyNumero = raw_input()
		print("Enter position:")
		posicion = raw_input()
		# add it to the list
		myPlayers.append(Player(nombre, edad, goals, jerseyNumero, posicion))
		print("Player was added.")
		print("What do you want to do? Enter the # and press Enter.") 
		print("(1) Add a player") 
		print("(2) Print all players")
		print("(3) Save your player list to a file")
		print("(0) Leave the program")
		choice = raw_input()

	# if choice is 2, then print the stats
	elif choice == "2":
		for player in myPlayers:
			#prints summary
			player.getPlayerSummary()
		print("What do you want to do? Enter the # and press Enter.")
		print("(1) Add a player") 
		print("(2) Print all players") 
		print("(3) Save your player list to a file")
		print("(0) Leave the program")
		choice = raw_input()

	# if choice is 3, save their players 
	elif choice == "3":
		print("What will be the name of your file? Enter the name with the .tmd at the end.")
		filename = raw_input()
		# save their players and file
		saveTeam(myPlayers, filename)
		print("Saved!")
		print("What do you want to do? Enter the # and press Enter.")
                print("(1) Add a player")
                print("(2) Print all players")
                print("(3) Save your player list to a file")
                print("(0) Leave the program")
		choice = raw_input()
	# if choice is 0, they should exit the program
	elif choice == "0":
		lul = False		
