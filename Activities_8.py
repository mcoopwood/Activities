
#Activity 8.1
num = int(input("Enter an integer between 1 - 15 "))
square_list = []

for x in range(0,num + 1):
    timed = x ** 2
    square_list.append(timed)

for num in square_list:
    print(num)

#Activity 8.2
Pete_scores = [187, 212, 199, 244, 215, 196, 238, 201]
counter = 0

for x in Pete_scores:
    if x > 200:
        counter += 1
print("There are " +str(counter) +" above 200")


for y in range(len(Pete_scores)):
    if Pete_scores[y] == max(Pete_scores):
        print("Pete's best games is in index position " +str(y))
   


# Activities 8.3
word_list = []

word = ''
while word != '0':
    word = input("Enter a word & type 0 to end ")
    word_list.append(word)


counter3 = 0 # counts the number of letters in a word
for z in word_list:
    counter3 += len(z)

print(counter3)

mean = counter3 / len(word_list)
print("Mean of letters is " +str(mean))