print("Converter call file")

def to_inches(cm):
    return cm*0.393701

def to_miles(km):
    return km*0.621371

def to_fahrenheit(celsius):
    return (celsius*9/5)+32


if __name__ == "__main__":
    print("Call a converting func that you want")
else:
    print("Was imported (not executed directly)")
