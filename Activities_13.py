def factorial(num: int) -> int:
    fact = 1
    for i in range(1,num + 1):
        fact = fact * i
    return fact

print("5! is", factorial(5))


def add_underscores(word:str) -> str:
    new_word = "_"
    for i in range(len(word)):
        new_word = new_word + word[i] + "_"
    return new_word

print(add_underscores("hello"))
print(add_underscores("python"))


number = 5
my_list = [5, 2, 12, 7, 3, 8]
low = []

for element in my_list:
    if element < number:
        low.append(element)

print(low)

def calculate_bmi(weight,height):
    return weight / (height**2)

patients = [[70, 1.8], [80, 1.9], [50, 1.6]]

for patient in patients:
    weight = patient[0]
    height = patient[1]
    bmi = calculate_bmi(weight, height)
    print(f"Patient's Bmi is: {bmi}")