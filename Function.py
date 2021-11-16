# function

# Example HelloWorld with function
def print_message(msg):
    print(msg)

print_message("Hello World")


def print_message(name):
    return "Hello world " + name
msg=print_message("Jim")
print(msg)

def print_message(age):
    return age > 18
msg=print_message(19)
print(msg)

def print_message(text):
    return text==text[::-1]
msg=print_message('aabaa')
msg=print_message('aabdaa')
print(msg)




