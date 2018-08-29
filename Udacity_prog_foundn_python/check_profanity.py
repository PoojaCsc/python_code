import urllib.request

def read_text():
    quotes = open(r"C:\Self\General\Pooja\Edu_Career\Learning\Python\Code\Udacity_prog_foundn_python\movie_quotes.txt") #built in function
    contents_of_file = quotes.read().split()
   #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    flag = 0
    for word in text_to_check:
        connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+word)
        output = connection.read()
       # print(output)
        if b"true" in output:     # file is opened in bytes mode and output is in byte so compare byte to byte
            flag= flag +1

    if flag > 0:
         print("profanity alert")
    else:
         print("the text has no curse words")

    connection.close()

read_text()