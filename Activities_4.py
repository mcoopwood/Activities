# in class activity
def my_function(a,b):
    result = a*b

    if result > 40:
        print("Big number!!!")
    else:
        print("Little number !!!!")

# Function for  4.1
def display_name(last,first):
   results = print('Name:' +last +',' +first)
   return results

# Function for 4.2
def double_square(number):
    d = number * 2
    s = number * number

    facts = 'The double value is '  + str(d) +', and the square value is ' + str(s)
    return facts

# Function for 4.3
def largest_number(num1, num2, num3):
    if num1> num2 and num1> num3:
        print(num1)
    elif num2> num1 and num2 > num3:
        print(num2)
    else:
        print(num3)


    # main

    #str x = 4
#y= 11
#my_function(x,y)

# Activity 4.1
firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")

display_name(lastname,firstname)

#Activity 4.2
fav = eval(input("Enter your favorite number: "))
result = double_square(fav)
print(result)

#Activity 4.3
number1 = eval(input("Enter a number: "))
number2 = eval(input("Enter a number: "))
number3 = eval(input("Enter a number: "))

largest_number(number1, number2, number3)

