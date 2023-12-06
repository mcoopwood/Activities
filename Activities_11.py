





houses = int(input("How many houses need to be carpeted tomorrow: "))
main_list = []
results = 0

for numberH in range(houses):
    roomNum = numberH + 1
    rooms = int(input("How many rooms to carpeted in house " +str(roomNum) +": "))
    House = []
    for numberR in range(rooms):
        rom = numberR + 1
        size = input("What are the dimensions of room " +str(rom) +": ")
        House.append(size)
    main_list.append(House)

print(main_list)

for house in main_list:
    for pair in house:
        footage = pair.split('x')
        num1 = int(footage[0])
        num2 = int(footage[1])
        total = num1 * num2
        results = results + total

print("Total footage needed " +str(results) +" sq ft")




