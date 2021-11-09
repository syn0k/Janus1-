# string formatting

if __name__ == '__main__':
    strhw = "Hello World"
    print("My first programm {}".format(strhw))

strhw0 = "Hello"
strhw1 = "World"
strhw2 = "HW"
print("My first programm {0} {1} {2}".format(strhw0, strhw1, strhw2))
print("My first programm {2} {1} {0}".format(strhw0, strhw1, strhw2))

pi = 3.1415
print("it's PI string formatting:{pi:1.2f}".format(pi=pi))  # is's PI 3.14

print(f"My first programm {strhw0} {strhw1} {strhw2}")
