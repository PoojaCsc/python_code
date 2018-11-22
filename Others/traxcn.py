#program to find out the number closest to zero. If there are same numbers in +ve and -ve then the o/p should be +ve

nums = []
abs_nums = []

n = int(input())
nums = list(map(int, input().split()))

if not nums:
    print("0")

for i in range(len(nums)):
    abs_nums.append(abs(nums[i]))

abs_nums.sort()


print(abs_nums[0])