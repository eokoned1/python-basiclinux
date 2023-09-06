"""
File:    file_system.py
Author:  Mofe Okonedo
Date:    12/1/22
Section: 14
E-mail:  eokoned1@umbc.edu
Description:
  File system, similar to Linux but in Python
"""


def pwd(home_dir):
    print(home_dir) #prints home directory from main function
def ls(directory_name_or_path):
    pass
def mkdir(directory_name):
    pass
def cd(directory_name_or_path):
    pass


def touch(file_name_path):
    if not "/" in file_name_path:
        split_pwd = present_working_directory.split("/") 
        result_dir = file_struct['/']
        for dir_name in split_pwd[1:-1]:
            if dir_name == '':
                dir_name = "/" 
            result_dir = result_dir[dir_name + "/"] 
            


        
        
        result_dir[file_name_path] = ''
        

    


def rm(file_name_path):
    pass
def locate(file_name):
    pass
def exit():
    return False #Stops program by returning false if user inputs "exit"


if __name__ == "__main__":
    

    present_working_directory = "/big_dir/inner_dir/"
    
    file_struct = {
        "/": { 
            "big_dir/": {
                'a1.txt':'', 
                'a2.txt':'',

                "inner_dir/": {
                    'a1.txt':'',
                    'b1.txt':''
                }
            },
            "other_dir/": {
                'd.txt':''
            },
            "c.txt":''


        }
    }
    print(file_struct["/"]["big_dir/"]["inner_dir/"])

    stop = True

    user_input = input("[cmsc201 proj3]$ ").split()
    while stop:
        if user_input[0] == 'pwd':
            pwd()
        elif user_input[0] == "ls":
            ls()
        elif user_input[0] == "mkdir":
            mkdir()
        elif user_input[0] == "cd":
            cd()
        elif user_input[0] == "touch":
            touch(user_input[1])
        elif user_input[0] == "rm":
            rm()
        elif user_input[0] == "locate":
            locate()
        elif user_input[0] == "exit":
            stop = exit()
        user_input = input("[cmsc201 proj3]$ ").split()

