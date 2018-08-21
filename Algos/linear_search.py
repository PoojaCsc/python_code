def search(ls, x):
   # print(x)
    for i in range(len(ls)):
       # print(ls[i])
        if ls[i] == x:
            return i

    return -1


def main():
    nums = []

    while True:
        ele = int(input("Enter the number:"))
        nums.append(ele)
        ch = input("Do you want to continue? y/n")
        ch = ch.lower()
        if ch == 'n':
            break

    n = int(input("enter the number to be searched?"))
  #  print(nums,n)
    result = search(nums,n)
   # print(result)
    if result == -1:
        print("number not found")
    else:
        print(f"Number found at the position {result+1}")

if __name__ == "__main__":
    main()

