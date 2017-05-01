def primeNums(myNum):
	for num in range(2,myNum):
		if myNum % num == 0:
			return False			
	return True
 
list = []

for number in range(2,10000):
	Waldo = primeNums(number)
	if Waldo == True:
		list.append(number)

my_file = open("primes.txt", "w")
my_file.write(str(list))
my_file.close()
print(list)

