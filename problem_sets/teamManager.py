class Player(object):

  def __init__(self, name, age, goals):
    self.name = name
    self.age = int(age)
    self.goals = int(goals) 
    
    
  def getPlayerSummary(self):
    summary = "Player Name: " + self.name + "\n"
    summary = summary + "Player Age: " + str(self.age) + "\n"
    summary = summary + "Goals Scored: " + str(self.goals) 
    return summary
    

#ISIS EXECUTION STARTS HERE 
players = []

#UI
keepRunning = True 
#While Loop Starts

while keepRunning: 

  print("(1) Add a player.")
  print("(2) Print all players.")
  print("(3) Print Average number of goals for all players.")
  print("(0) Leave the program and delete all players.")
  #variable for user input
  response = input()
  if response == 0:
    keepRunning = False
    
  elif response == 1:
    #options 
    print("Enter name:")
    pName = input()
    print("Enter age:")
    pAge = input()
    print("Enter number of goals scored this season")
    pGoals = input() 
    
    myPlayer =  Player(pName, pAge, pGoals)
    #added info
    players.append(myPlayer)
    print("Ok, player entered.")
    
  elif response == 2:
    
    for things in players:
      print(things.getPlayerSummary())  
