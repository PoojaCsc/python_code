
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


def selection_sort(ilist):
    len_list = len(ilist)
    for i in range(len_list):                   
        min = i
        for j in range(i+1,len_list):
            if ilist[j] < ilist[min]:
                min = j
        tempo = ilist[i]
        ilist[i] = ilist[min]
        ilist[min] = tempo



if __name__ == "__main__":
    main()
