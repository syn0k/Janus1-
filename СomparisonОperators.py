# comparison operators
if __name__ == "__main__":
    print(2 > 1)  # True
    result = 2 > 1
    type(result)  # print True

    print(2 > 2)  # False
    print(2 >= 2)  # True
    print(3 >= 2)  # True
    print(3 >= 4)  # False
    print(1 != 1)  # False

    # string operations are case sensitive
    x = "String"
    y = "string"
    print(x.lower() == y.lower())  # strings are equal = True


    print(1 < 2 < 3)  # True
    print(1 < 2 and 2 < 3)  # True
    print(1 > 2 and 2 < 3)  # False

    is_admin = False
    if not is_admin:
        print("Not an admin")
    if is_admin == False:
        print("Not an admin")
