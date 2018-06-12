numbers = []
def main():

while True:
    num = intput("Please enter a no.")
    numbers.append(num)
    choice=input("Do you want to continue?Y/N")
    if choice == "Y":
        continue
    else:
       break

def selection(numbers):
    for i in range(len(numbers)):
