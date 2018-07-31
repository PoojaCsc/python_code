import os

def rename_files():
    # get file names from a folder
    file_list = os.listdir(r"C:\Self\General\Pooja\Edu_Career\Learning\Python\Code\Udacity_prog_foundn_python\prank\prank") #r means process as it is
    # os.listdir Return a list containing the names of the entries in the directory given by path
    print(file_list)
    saved_path = os.getcwd()
    print(f"The current working directory is {saved_path}")
    os.chdir(r"C:\Self\General\Pooja\Edu_Career\Learning\Python\Code\Udacity_prog_foundn_python\prank\prank")

    for file_name in file_list:
        os.rename(file_name,)

rename_files()