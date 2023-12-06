import random
def password():
    #passw = input("Create a password")
    run = 0
    while(run != 1):
        passw = input("Create a password ")
        if len(passw) >= 9:
            for i in range(len(passw)):
                if passw[i] in '1234567890':
                    run += 1
                    return (passw)

password = password()
print("This is your new password: " +password)


#Mid-term review 2
Friend_list = []
With_e = []
without_e = []

frien1 = input("Enter the name of friend: ")
Friend_list.append(frien1)

frien2 = input("Enter the name of friend: ")
Friend_list.append(frien2)

frien3 = input("Enter the name of friend: ")
Friend_list.append(frien3)

frien4 = input("Enter the name of friend: ")
Friend_list.append(frien4)

for n in Friend_list:
    for i in n:
        if i == 'e':
            With_e.append(n)
            break

    if n not in With_e:
        without_e.append(n)

print("Friend names with e:  ")
print(With_e)
print("Friend names without e ")
print(without_e)

#3

computer_choice = random.choice(["Rock", "Paper", "Scissors"])
user = input("Enter: Rock, Paper, Scissors")

if computer_choice == user:
    print("Tie")