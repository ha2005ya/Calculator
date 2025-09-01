print("Menu:")
print("1: Add")
print("2: Subtract")
print("3: Multiply")
print("4: Divide")
print("5: Modulus")
choice = int(input("Enter your choice (1-5): "))

if 1 <= choice <= 5 :
	num1 = float(input("Enter your number: "))
	num2 = float(input("Enter your number: "))
	
	if choice == 1 :
		result = num1 + num2
		print("Result: %.2f + %.2f = %.2f" % (num1, num2, result))
		
	elif choice == 2 :
		result = num1 - num2
		print("Result: %.2f - %.2f = %.2f" % (num1, num2, result))
		
	elif choice == 3 :
		result = num1 * num2
		print("Result: %.2f * %.2f = %.2f" % (num1, num2, result))
		
	elif choice == 4 :
		if num2 != 0 :
			result = num1 / num2
			print("Result: %.2f / %.2f = %.2f" % (num1, num2, result))
		else :
			print("Error: Division by zero.")
			
	elif choice == 5 :
		if num2 != 0 :
			result = num1 % num2
			print("Result: %.2f %% %.2f = %.2f" % (num1, num2, result))
		else :
			print("Error: Modulus by zero.")
			
	else :
		print("Error: Invalid choice. ")