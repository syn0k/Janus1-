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
# delete file :) relax
import os


def check_exist_file():


    def delete_exist_file():


    def create_file():


def write_file():
    file = open("test.txt", "a")
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


def delete_file():
    os.remove("test.txt")


if __name__ == "__main__":