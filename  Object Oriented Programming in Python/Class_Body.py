# global var
PYTHON_PROGRAMMERS = 3
DEVOPSS = 8
REACT_DEV = 2

class DepartmentIT:
    # class var
    PYTHON_PROGRAMMERS = 4
    DEVOPSS = 3
    REACT_DEV =6

    # self
    def DepartmentIT_Info_self(self):
        print(self.PYTHON_PROGRAMMERS, self.DEVOPSS, self.REACT_DEV)

    # class
    def DepartmentIT_Info_class(self):
        print(DepartmentIT.PYTHON_PROGRAMMERS, DepartmentIT.DEVOPSS, DepartmentIT.REACT_DEV)

    @property
    def DepartmentIT_Info_property(self):
        print(self.PYTHON_PROGRAMMERS, self.DEVOPSS, self.REACT_DEV)

    @classmethod
    def DepartmentIT_Info_classmethod(cls):
        print(f'DepartmentIT_Info_classmethod {cls.PYTHON_PROGRAMMERS} {cls.DEVOPSS} {cls.REACT_DEV}')

    @staticmethod
    def DepartmentIT_Info_staticmethod():
        print(f'DepartmentIT_Info_staticmethod {DepartmentIT.PYTHON_PROGRAMMERS} {DepartmentIT.DEVOPSS} '
              f'{DepartmentIT.REACT_DEV}')

    def Python_pr(self):
        print('Python_pr')

    def Devopss(self):
        print('Devopss')

    def add_Python_pr(self):
        self.PYTHON_PROGRAMMERS = self.PYTHON_PROGRAMMERS +1
        DepartmentIT.PYTHON_PROGRAMMERS = DepartmentIT.PYTHON_PROGRAMMERS +1

it = DepartmentIT()
it.DepartmentIT_Info_self()
it.DepartmentIT_Info_class()
it.DepartmentIT_Info_property
it.DepartmentIT_Info_classmethod()
it.DepartmentIT_Info_staticmethod()

print(it.PYTHON_PROGRAMMERS)
it.add_Python_pr()
print(it.PYTHON_PROGRAMMERS)




