print("How many people are coming to the party?")
people = int(raw_input())


print("How many donuts will you have at your party?")
donuts = int(raw_input())


donuts_per_person = donuts / people


print("Our party has " + str(people) + " people and " + str(donuts) + " donuts.")


print("Each person at the party gets " + str(donuts_per_person) + " donuts.")
