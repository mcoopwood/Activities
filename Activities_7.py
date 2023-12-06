my_name = "New York"
count = 0

for char in my_name:
    count += 1

print("There are " +str(count) +" character in " +my_name)
print(my_name[2])

string1 = "wrriognhgt"
num = string1[1::2]
print(num)

name1 = "Julio Rodriquez"
name2 = "Rosa Luxemburg"

first = name1[0:5]
last = name2[5:]
print(first +" " + last)




def vowel(string: str) -> int:
    count = 0
    if len(string) == 0:
        return 0
    else:
        if string[0] in 'aeiou':
            return 1 + vowel(string[1::])
        else:
            return 0 + vowel(string[1::])
count = vowel("raspberry")


string = "raspberry"
vowel(string)
print(count)