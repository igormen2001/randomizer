import random
print("welcome to super randomizer\n======================================================")
data = input("please enter a max number: ")
if data == "":
	data = 10
number = random.randint(0,int(data))
print("here`s your random number ")
print(number)
