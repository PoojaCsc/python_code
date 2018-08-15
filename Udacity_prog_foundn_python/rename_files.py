import os

def rename_files():
    # get file names from a folder
    file_list = os.listdir(r"C:\Self\General\Pooja\Edu_Career\Learning\Python\Code\Udacity_prog_foundn_python\prank\prank") #r means process as it is
    # os.listdir Return a list containing the names of the entries in the directory given by path
    print(len(file_list))
    for file_name in file_list:
        print(file_name)

    saved_path = os.getcwd()
    print(f"The current working directory is {saved_path}")
    os.chdir(r"C:\Self\General\Pooja\Edu_Career\Learning\Python\Code\Udacity_prog_foundn_python\prank\prank")
    translation_table= str.maketrans("0123456789","          ")  #make a tranlation table mapping the change


    for file_name in file_list:
        print("old name - "+file_name)
        print("old name - "+file_name.translate(translation_table))     #translate acc to the translation table
        os.rename(file_name,file_name.translate(translation_table))

rename_files()