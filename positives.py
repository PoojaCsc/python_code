nums = [1,23,21,5,8,0,1,7,0,6,5,2,3]
numbers = []
zeroes = []
for n in nums:
    if  n == 0:
        zeroes.append(n)
    else:
        numbers.append(n)

print(numbers + zeroes)
