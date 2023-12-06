# TonyaS = input("Tonya How many shirts do you have?")
# TonyaP = input("Tonya How many pants do you have?")
# TonyaH = input("How many hats to you have?")
#
#         SalS = input("How many shirts do you have?")
#         SalP = input("How many pants do you have?")
#         SalH = input("How many hats to you have?")
#
#         YouS = input("How many shirts do you have?")
#         YouP = input("How many pants do you have?")
#         YouH = input("How many hats to you have?")
#
#         TotalS = TonyaS + SalS + YouS
#         TotalP = TonyaP + SalP + YouP
#         TotalH = TonyaH + SalH + YouH

# Activity 1
# housemates = ["You","Tonya","Saleem"]
#
#
# coupon = 0
# for name in ["Melanee","Tonya", "Saleem"]:
#     for clothes in ["shirts", "pants", "hats"]:
#         n = input(name + " how many " + clothes + " do you have?")
#         coupon = coupon + int(n)
#
# print(str(coupon) + " is the answer")

# Activity 2
"""paid = 0
meals = int(input("How many meals did you eat yesterday: "))
for meal in range (meals):
    price = input("How much did you pay for each meal?: ")
    paid = paid + int(price)

print("You paid a total of $" +str(paid))
"""

# Activity 3
great = 2
nice = 1
bad = -1
horrible = -2

total = 0
for day in range(7):
    answer = input("How's the weather?")
if answer == "great":
    total = total + 2
elif answer == "nice":
    total = total + 1
elif answer == "bad":
    total = total - 1
elif answer == "horrible":
    total = total - 2
else:
    print("try again")


if total > 5:
    print("you have a great week")
elif total >=0:
    print("You had a lousy week")
elif total < 0:
    print("you had a putrid week")