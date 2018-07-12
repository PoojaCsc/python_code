
def main():
    numbers = []
    while True:
        num = input("Please enter a no.")
        numbers.append(num)
        choice=input("Do you want to continue?Y/N").upper()
        if choice == "Y":
            continue
        else:
            break
    print(f"The numbers you entered are:{numbers}")
    selection_sort(numbers)
    print(f"The sorted numbers are :{numbers}")


def selection_sort(mylist):
    len_list = len(mylist)
    for i in range(len_list):
        min = i
        for j in range(i+1,len_list):
            if mylist[j] < mylist[min]:
                min = j
        mylist[i],mylist[min] = mylist[min],mylist[i]



if __name__ == "__main__":
    main()
