

contents = open('veggies.txt', 'r')
twoWord = []

for vegetable in contents:
    word = vegetable.split()
    if len(word) != 1:
        twoWord.append(vegetable)

print(twoWord)

#Activity 2

outfile = open('favfood.txt', 'w')
food = []

command = ''
while(command != 'Stop'):
    command = input("Please enter a favorite food or type Stop ")
    if command != 'Stop':
        food.append(command)

for item in food:
    string = item + ','
    outfile.write(string)

print(food)

#Activity 3

mainFood = []


numpeople = int(input("How many people are coming to the party "))

for food in range(numpeople):
    list = []
    nums = food + 1
    entrees = input("How many entrees from person " +str(nums) +" ")
    list.append(entrees)

    sides = input("How many sides from person " +str(nums) +" ")
    list.append(sides)

    desserts = input("How many desserts from person " +str(nums) +" ")
    list.append(desserts)
    mainFood.append(list)

print("The mainFood list is: " +str(mainFood))