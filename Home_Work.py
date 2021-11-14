# # Home Work
try:
    PleaseInput = input('Please input the number\n')
    # print(type(PleaseInput))
    PleaseInput_int = int(PleaseInput)
    # print(type(PleaseInput_int))

    ch = ''
    x = 0
    while x < PleaseInput_int:
        x += 1
        ch += "*"
        print(ch)

except ValueError:
    print("That's not an int!\nPlease input the number\n")
