# in bubble sort we compare the adjacent elements and swap them acc to whether it is in ascending or descending.
# This way the highest or the lowest element bubbles to the top that is the end of the array


def bubble_sort(ls):
    for i in range(len(ls),0,-1):
        for j in range(0,i-1,1):
            if ls[j] > ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]

    return ls

def main():
    arr = [4,7,2,9,0,1]
    sor_arr = bubble_sort(arr)
    print(sor_arr)


if __name__ == "__main__":
    main()





