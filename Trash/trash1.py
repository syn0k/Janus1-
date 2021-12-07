# ['__add__'
# '__class__'
# '__class_getitem__'
# '__contains__'
# '__delattr__'
# '__delitem__'
# '__dir__'
# '__doc__'
# '__eq__'
# '__format__'
# '__ge__'
# '__getattribute__'
# '__getitem__'
# '__gt__'
# '__hash__'
# '__iadd__'
# '__imul__'
# '__init__'
# '__init_subclass__'
# '__iter__'
# '__le__'
# '__len__'
# '__lt__'
# '__mul__'
# '__ne__'
# '__new__'
# '__reduce__'
# '__reduce_ex__'
# '__repr__'
# '__reversed__'
# '__rmul__'
# '__setattr__'
# '__setitem__'
# '__sizeof__'
# '__str__'
# '__subclasshook__'
#
# 'append'
# 'clear'
# 'copy'
# 'count'
# 'extend'
# 'index'
# 'insert'
# 'pop'
# 'remove'
# 'reverse'
# 'sort']

ls = [1,2,3,4,5,6,7,8,9,0]
print(dir(ls))
print(ls.__iter__())
asd = ls.__iter__()
print(dir(asd))
print(type(asd))
print(type(ls))
#
# for i in ls:
#     print(i)
#     print(dir(i))
#     print(type(i))

