def swap_indices(list, num1, num2):
    aux = list[num1]
    list[num1] = list[num2]
    list[num2] = aux

    return list

list = ["Action", "Suspense", "Romance", "Comedy","Scifi", "Animation", "Fantasy"]
num1 = 0
num2 = 1

print(swap_indices(list, num1, num2))