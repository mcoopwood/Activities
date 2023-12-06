# in class exercise
jar = True
count = 0
while(jar == True):
    count += 1
    user =input("Does the jar still contain beans?")
    if user == "no":
        jar = False
print("The jar contains"+ str(count)+"beans")


# exercise 3.1
vote = 2

while vote == 2:
    candidate = input("Choose your candidate: A,B, or C ")

    if candidate == "Candidate A":
        print("You voted for Candidate A!")
        vote += 1

    elif candidate == "Candidate B":
        print("You voted for Candidate B!")
        vote += 1

    elif candidate == "Candidate C":
        print("You voted for Candidate C!")
        vote += 1
    else:
        print("You didn't vote correctly. Try Again")

# in class exercise
for num in range(2,10):
    print(num)
    print("Wow")


# exercise 3.2
for x in range(7,12):
    x *= x
    print(x)
