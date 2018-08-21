def binary_search(ls, num):
    start = 0
    end = len(ls) - 1

    for i in range(len(ls)):
        mid = (int)((start + end)/2)
        if num == ls[mid]:
            return mid
        elif num < ls[mid]:
            end = mid - 1
        elif num > ls[mid]:
            start = mid + 1
    return -1





def main():
    ele = [2,5,8,12,45,89]
    n = 89
    res = binary_search(ele,n)
    if res < 0 :
        print("element not found")

    else:
        print("element found at ", res+1)



if __name__ == "__main__":
    main()

