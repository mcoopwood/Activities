
def linear_search(L,e):
    """
    :param L: a list of elements
    :param e: a particular element
    :return: true if e is in L and False otherwise
    """

    for word in range(L):
       for letter in range(word):
        if L[letter] == e:
           print("e is in position " +letter)



#trying to do a search
def search(List, mainnum):



   # print(middle)

    lower = 0
    upper = len(List)-1

    while True:
        middle = (upper+lower)//2

        if mainnum > List[middle]:
            lower = middle +1
        elif mainnum < List[middle]:
            upper = middle-1
        else:
            print(str(mainnum) + " was found at postion " + str(middle))
            break

        """ 
    if mainnum > holder:
        for num in List[middle:]:
            print(num)
            if num == mainnum:
                position = List.index(num)
                print(str(mainnum) + " was found at postion " + str(position))
                
    elif mainnum < holder:
        for num in List[:middle]:
            if num == mainnum:

   """


search([8, 13, 16, 17, 22, 25, 30, 60, 83, 107], 30)