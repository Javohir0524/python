###################################

name = input("Enter your name: ")

if name == "":
	print("You did not enter your name.")
else:
	print(f"Hello {name}")


###################################


name = input("Enter your name: ")

while name == "":
	print("You did not enter your name.")
	name = input("Enter your name: ")
print(f"Hello {name}")


####################################


for i in range(1, 11):
	print(i)

for i in reversed(range(1, 11)):
	print(i)

print("Have a good day!")

#######################################

credit_card = "1234-5678-9012-3456"

for i in credit_card:
	print(i)
	
#######################################

for i in range(1, 40):
	if i == 35:
		continue
	else:
		print(i)
		
#######################################

for i in range(1, 50):
	if i == 45:
		break
	else:
		print(i)
		
#######################################