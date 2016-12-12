months = 0
ticket = 60

while ticket > 0:
	print("Have you paid your ticket? yes/no")
	response = raw_input()
	if response == "yes":
		ticket = 0
else:
	 ticket = ticket * 2
print("Ok, your ticket is now now "  +  str(ticket))
	
