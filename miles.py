message = input("Hello User, Welcome To Sublime")
name = input("Please enter your name:")
print(f"\nHello, {name}!")
print()
def convert_distance (miles):
	km = (float)(miles * 1.6)
	return km
while True:
	try:
		miles = float(input("Please enter miles you drove:"))
		break
	except:
		print("Invalid input, try again.")
print()
result = convert_distance(miles)
print()
print("The distance in Kilometers that you drove is: " +str(result))
print()
print(f"\n Thank you, {name}.")

