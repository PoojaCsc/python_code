# program to split a list of words into letters and there should be no duplicates
## the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        if aletter not in letterlist:
            letterlist.append(aletter)
print(letterlist)