# take input number
num = int(input())

# run a loop from 1 to that number


for i in range(1,num):
    #take the current number and divide it from numbers 1 to itself.If it is divisible by exactly 2 numbers it is prime, i.e. 1 and number itself
    j = 1
    count = 0
    while j <= i:
        if i%j == 0:
           count = count +1
        j = j + 1

    # check if count is equal to 2

    if count == 2:
        print(i, end = " ")







