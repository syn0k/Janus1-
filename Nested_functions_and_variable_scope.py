#example 1
greeting = "Hello from the global scope"

def greet():
    greeting = "Hello from the enclosing scope"

    def nested():
        greeting = "Hello from the local scope"
        print(greeting)
    nested()

greet()
print(greeting)


#example 2
print('#example 2')
greeting = "Hello from the global scope"
def greet(greeting):
    print(f'Greet in func:{greeting}')

    greeting = "Hello from the enclosing scope"

    print(f'Greet in func:{greeting}')

    def nested():
        greeting = "Hello from the local scope"
        print(greeting)
    nested()

greet('test')
print(greeting)




