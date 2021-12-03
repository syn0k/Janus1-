class Employee:
    def __init__(self, first_name: str, last_name: str, salary: int):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def from_string(cls, srt_):
        first_name, last_name, salary = srt_.split("-")
        return cls(first_name, last_name, int(salary))


emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")

print(emp1.first_name)
print(emp1.salary)
print(emp1.last_name)

print(emp2.first_name)
print(emp2.salary)