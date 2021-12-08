class A:
 def some_method(self):
    print('some_method A')

class B(A):
     def some_method(self):
        print('some_method B')

x = B()
x.some_method() # some_method B


class A:
    def some_method(self):
        print('some_method A')

class B(A):
    def some_method(self):
        super().some_method()
        print('some_method B')

x = B()         # some_method A
x.some_method() # some_method B