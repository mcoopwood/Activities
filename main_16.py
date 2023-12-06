import calculator_16


num1 = int(input("Enter an integer "))
num2 = int(input("Enter another integer "))
num3 = int(input("Enter 1 to add, 2 to subtract, 3 to multiply, and 4 to divide "))

if num3 == 1:
    calculator_16.addition(num1,num2)
elif num3 == 2:
    calculator_16.subtraction(num1,num2)
elif num3 == 3:
    calculator_16.multiplication(num1, num2)
elif num3 == 4:
    calculator_16.division(num1,num2)
else:
    print("Wrong option")

