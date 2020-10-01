print("************DRIVING ELIGIBILITY TEST************")
print("\t")


while (true):
	age= float(input("enter your age:"))
		
	if age>18 and age<81:
		print("you are eligible to drive")

	elif age==18:
		print("Please come to our association to tell if you are physically eligible to drive")

	elif age>8 and age<18:
		print("you are too smaller to drive")

	else:
		print("the entered age will not be considered")
