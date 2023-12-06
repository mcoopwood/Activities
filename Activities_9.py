
Tshirts = {'black': 3, 'blue': 4, 'red': 2, 'white': 2, 'pink': 3}
print(Tshirts)

color = input("What color Tshirt will you change? ")
maths = input("Would you like to 'add' or 'subtract' ? ")
number = input("How many " +color +" T shirts to " +maths +"? ")

for y in Tshirts:
    if y == color and maths == 'add':
        Tshirts[y] += number
    elif y == color and maths == 'subtract':
        Tshirts[y] -= number

print(Tshirts)
