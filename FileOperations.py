# file operations
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# script
# check file exist, if exist then delete file, create file
# write text in file "bla bla bla"
# read the file and print text
# add text in file "bla2 bla2 bla2"
# read the file and print text
# read current directory
# delete file :) relax
import os


# list file
def list_current_directory_files():
    for entry in os.listdir():
        print(entry)


def check_exist_file():
    try:
        file = os.path.exists("test.txt")
        if file == True:
            print("File exists")
    except:
        print("File NOT exists")


def create_file():
    file = open("test.txt", "a")
    file.close()


def write_file():
    file = open("test.txt", "w")
    file.write("Write file information - bla bla bla\n")
    file.close()


def read_file():
    file = open("test.txt", "r")
    for entry in file:
        print(entry)

def add_write_file():
    file = open("test.txt", "a")
    file.write("Write file information - bla2 bla2 bla2\n")
    file.close()


def delete_exist_file():
    try:
        os.remove("test.txt")
    except:
        print("File not exists")


if __name__ == "__main__":
# delete_exist_file()
# check_exist_file()
# list_current_directory_files()
