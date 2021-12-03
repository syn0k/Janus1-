class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.strip().capitalize()
        self.last_name = last_name.strip().capitalize()
        self.full_name = self.first_name+" "+self.last_name
        self.initials = self.first_name[0]+"."+self.last_name[0]

a1 = Name('john', 'SMITH')
print(a1.first_name)
print(a1.last_name)
print(a1.full_name)
print(a1.initials)