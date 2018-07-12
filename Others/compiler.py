from sys import argv

script, filename = argv

input_file = open(filename)
if filename

tokens = input_file.read().split()

#print(tokens)

for i in range(len(tokens)):
    #print(tokens[i])
    if tokens[i] == '+':
        num1 = int(tokens[i-1])
        num2 = int(tokens[i+1])
        print(num1 + num2)
