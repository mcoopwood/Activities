def program(n):
    if n==0:
        return 5
    else:
        print(n)
        return (program(n-1)) * 10



    #main

answer = program(4)

print(answer)