sum = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(f"The sum of all the multiples of 3 or 5 under 1000 is {sum}")
