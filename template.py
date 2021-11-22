# Syntactic sugar
#print(walrys := True)

# input1 = int(input("Enter the number"))
# for x in range(input1):
#     print('*' * (x+1))



for x in range(input1 := int(input("Enter the number"))):
    print('*' * (x+1))

