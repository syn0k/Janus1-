# :=

value = input(" Please enter something: ")

while value != '':
    print("Nice")
    value = input(" Please enter something: ")

# use walrus
while (value := input(" Please enter something: ") !=''):
    print("Nice")

