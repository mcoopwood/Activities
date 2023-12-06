def myfunction(x:str) -> str:
    answer: str = ""
    index: int = len(x)-1
    for putInPlace in range(len(x)):
        answer = answer + x[index]
        index = index - 1
    return answer



def myfunction2(x:str) -> str:
    answer: str = "" # holding place for string characters
    index: int = len(x) - 1 # the index for the string starting from last character

    while index != -1:
        answer = answer + x[index]
        index = index - 1
    return answer


def myfunction3(x):
    index: int = len(x) - 1  # the index for the string starting from last character

    if index == 0:
        return x

    else:
        return x[index] + myfunction3(x[:index])




print(myfunction('bobcats!'))

print(myfunction2('bobcats!'))

print(myfunction3('bobcats!'))

# answer to part 2: Mutability
fruits = ['pear', 'kiwi']
foods = [['rice', 'beans'], fruits, ['spam', 'bacon']]
print(foods)
# fruits in the list is a variable and output would be the content of the variable
[['rice', 'beans'], ['pear', 'kiwi'], ['spam', 'bacon']]

fruits[0]= 'apple'
print(foods)
#the first index in the fruits list is changed
[['rice', 'beans'], ['apple', 'kiwi'], ['pear', 'plums']]


fruits = ['grape', 'banana']
print(foods)
#foods is using the first fruit variable and not the second
[['rice', 'beans'], ['pear', 'kiwi'], ['spam', 'bacon']]

foods[2] = fruits
fruits[1] = 'plum'
print(foods)
#Fruits replaces the third index and the second imput of fruit is changed
[['rice', 'beans'], ['pear', 'plums'], ['pear', 'plums']]


""" 
for a in pg 3 maybe compare each letter to the first letter and then check and see
if word compares 
maybe keep check of index #
"""