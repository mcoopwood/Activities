"""
DocTest

>>> act2([1,2,3], [2,2,2])
12

>>> act4('RanDoM')
'RANDOM'

>>> act4("num6s")
'NUM6S'

"""




def my_sqrt(x):
    assert x > 0, "Input is negative"
    assert isinstance(x,int) or isinstance(x,float), "Wrong input type"
    y = x ** 0.5

    return y

def act2(list1, list2):
    assert len(list1) == len(list2), "Lists are different length"
    holder = []  # holds the multiplied numbers
    place = 0

    for i in range(len(list1)):
        try:
            mult = list1[i] * list2[i]
            holder.append(mult)
        except ZeroDivisionError:
            print("Multiplying " +list1[i] +" & " +list2[i] +" results in NaN")
        except TypeError:
            print("Wrong type for either " +list1[i] +" or " +list2[i])

    for num in holder:
        place += num

    return place

def act3(num):
    assert num > 0, "Number is not a valid integer"
    assert int(num), "Number is not a valid integer"

    sqrt = num * num

    return sqrt

def act4(word:str):
    assert str(word), "Input is not a string"
    holder = ''
    for letter in range(len(word)):
        upper = word[letter].upper()
        holder += upper

    return holder


