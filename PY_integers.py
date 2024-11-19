num1 = int(input("Enter number: ", ))

num2 = int(input("Enter second number: ", ))



choice = input(" Choose from the following - \n addition \n subtraction \n multiplication \n division \n modulus \n exponentiation \n floor_division \n", )

if choice == "addition":
    addition_result = num1 + num2
    print("addition:", addition_result)

elif choice == "subtraction":
    subtraction_result = num1 - num2
    print(subtraction_result)

elif choice == "multiplication":
    multiplication_result = num1 * num2
    print(multiplication_result)

elif choice == "division":
    division_result = num1/num2
    print(division_result)

elif choice == "modulus":
    modulus_result = num1%num2
    print(modulus_result)

elif choice == "exponentation":
    exponentiation_result = num1 ** num2
    print(exponentiation_result)
    
elif choice == "floor_division":
    floor_divsion_result = num1 // num2
    print(floor_division_result)

else:
    print("Error. Please provide  valid choice")

