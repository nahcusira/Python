
while True:
	num1 = input("Enter the integral part: ")
	try:
		num2 = input("Enter the fraction: ")
		if int(num2) < 0:
			print("The fraction must be a positive number.")
			continue
	except :
		print("The fraction must be a positive number.")
		continue
	print("Real number: " + num1 + "." + num2)
