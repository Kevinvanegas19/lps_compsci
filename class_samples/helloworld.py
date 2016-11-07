print("How many miles do you live from Richmond State?")
miles = int(raw_input())

print("What is your GPA?")
GPA = float(raw_input())

if miles <= 30 and GPA >= 2.0:
	print("Congrats, you're accepted to this crap school.")
if miles <= 30 and GPA < 2.0:
	print("Sorry")
else: 
	if miles > 30:
		print("What is your ACT score")
		ACT = int(raw_input())

	if ACT >= 18:
		print("Welcome to Richmond State.")
	if ACT < 18:
		print("Sorry, try a community college...")
	
