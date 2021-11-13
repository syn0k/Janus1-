# namedtuple is a subclass of tuple,
# which is used to create tuple-like objects with named fields and fixed length.
from collections import namedtuple

namedcars = [('car1', 1999, 2003), ('car2', 2002, 2012), ('car3', 1990, 2020)]

print(type(namedcars))  # <class 'list'>

# but
namedcar = namedtuple('car', 'name, year_start year_end')
namedcars = [namedcar('BMW', 1999, 2003), namedcar('BMW2', 2002, 2012), namedcar('BMW2', 1990, 2020)]

print(f'Print type - {type(namedcars)}')
print(f'Print get index - {namedcars[0]}')
print(f'Print get index - {namedcars[-1]}')
print(f'Print get index and attribute - {namedcars[0].name}')
