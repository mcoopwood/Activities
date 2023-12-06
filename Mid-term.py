"""
Question 1:
This code will generate an error because the variable used in the print statement
is a int and print can only execute str.


Question 2: > come back to unsure of cons
Pros
Lists: is ordered, can be changed, usually only has one data type, mutable
Dictionaries: matches data to other data, can use the key to instance retrieve
the value

Cons
Lists: index starts at 0
Dictionaries: unordered


Questions 3:
The code will not accomplish its task because the list that the names with
A are being appended to does not exist due to a typo in the spelling of friends.


Question 4: >??
Using the greater or equal to sign could be used to endure there is only one
grade for Rose.
"""

# Question 5
vegetables = {'eggplant':5, 'squash':7, 'arugula':2}

def produce():
    addp = ''
    
    while(addp != 'STOP'):
        addp = input("If you want to add produce, please type the vegetable, or STOP: ")
        if addp == 'STOP':
            break
        else:
            vegetables[addp] = 1
    print(vegetables)



# Question 6
def some_math(list)-> float:
    ok = [0]
    prod = [1]
    for n in list:
        sumz = ok[0]+ n # adds the numbers to each other starting with zero
        ok.insert(0,sumz) #inserts the total and the new number will be added with each loop

        products = prod[0] * n
        prod.insert(0,products)
    

    print("The sum of the floats is: " +str(sumz))
    print("The product of the floats is: " +str(products)) 


# Question 7
def marsh_vacay(city):
    
    count = 0
    vowels = 0 
    
    if len(city) >= 8 and len(city)%2 == 0:# at least 8 letters and even number of letters
        for n in city:
            if n == 'e' and city[3] != 'i': # has an e and does not have i as 4th character
                count += 1
            if n in 'aeiou': 
                vowels +=1

    if vowels%2 == 0 and count >1:
        print("The Marsh family can visit!")
    else:
        print("The Marsh family cannot visit")
    

#Question 8

def more_math(number):
    
    lits = []
    
    if number > 0: # makes sure number is positive 
        lits.append(number)

    for n in range(1,number):
        mathy = (n*4) - 2
        lits.append(mathy)

    print(lits)


# Question 9
def roomies():
    bowling_scores = {}

    name = ''
    while(name != 'STOP'):
        name = insert("Please enter your name and a bowling score, when done type STOP: ")

# Question 10
def add_more(num):
    Lits =[0]
    
    while(num >= 1):
        crossed = num **(-1)
        addition = crossed + Lits[0]
        Lits.insert(0,addition)
        newnum = num -1
        print(addition)
        return add_more(newnum)
    
# main 
produce()

my_list = [19.92, 2.7, 13.125, 8.63]
some_math(my_list)

place = input("What city should the Marsh family vist?")
marsh_vacay(place)

num = int(input("Enter a number "))
more_math(num)

number = int(input("Enter a number "))
add_more(number)

