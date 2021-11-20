#A variable is only available from inside the region it is created. This is called scope.

#example 1
#global scope
greeting = "Hello from the global scope"
x: int = 1

def greet():
    #enclosing scope
    greeting = "Hello from the enclosing scope"

    def nested():
        #local scope
        greeting = "Hello from the local scope"
        print(greeting)
    nested()

greet()
print(greeting)


#example 2
print('#example 2')
#global scope
greeting = "Hello from the global scope"
def greet(greeting):
    print(f'Greet in func:{greeting}')
    #enclosing scope
    greeting = "Hello from the enclosing scope"

    print(f'Greet in func:{greeting}')

    def nested():
        #local scope
        greeting = "Hello from the local scope"
        print(greeting)
    nested()

greet('test')
print(greeting)



