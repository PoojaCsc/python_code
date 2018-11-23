# Given an array of one's and zero's convert the equivalent binary value to an integer.
#
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
def binary_array_to_number(arr):
    arr.reverse()
    num = 0
    power = 0
    for ele in arr:
        num = num + ele*(pow(2,power))
        power = power + 1
    return num

    # return int("".join(map(str, arr)), 2)    map(fun, list) applies fun to every ele in list . str() converts to string
#>>>arr = [1,1,0,1]
#>>>print("".join(map(str,arr)))
#>>>1101
#>>>num = "".join(map(str,arr))
#>>>print(int(num,2))
#>>>13

binary = [0,1,0,1]
print(binary_array_to_number(binary))