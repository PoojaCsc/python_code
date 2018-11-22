# program to remove adjacent duplicate letters of even count

str = "cbbbaaaabbbccc"    # empty string
#str = "aabbdbcfffhskk"     # d

def remUtil(str):
    i = 0
    ind = 0
    while i < (len(str)-1):
        j = 0
        if str[i] == str[i + 1]:
            j = i
            ind = i
            count = 0
            while j < len(str)-1 and str[j] == str[j + 1]:
                count = count + 1
                j = j + 1
                i = i + 1
            # if the no. of comparisons are odd then even letters compared
            if count % 2 != 0:
                str = str[:(ind)] + str[(ind + count) + 1:]
                str = remUtil(str)
                #print(str)
                #remUtil(str)


        else:
            i = i + 1
    return str







print(remUtil(str))











