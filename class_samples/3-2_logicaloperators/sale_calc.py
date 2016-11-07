

print("Hi! What's your SAT score?")
score = int(input())
 
 
if score >= 700 and score < 1000:
  print("Welcome to SAT prep class!")
elif score < 1200:
  print("Thanks for coming, but you probably don't need this class.")
elif score == 1600:
  print("Whoa, you *really* don't need this class. Nice work.")
else:
  print("You must be lying. The top score on the ACT is 1600!")

