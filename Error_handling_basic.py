#Error handling basic
print('Error handling basic: Example: 1')

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as ex:
        print(f'On error occured: {ex}')
    except:
        print('Error occured')

print('Error handling basic: Example: 1')
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

#Throwing exceptions. Custom types of exceptions.
print('Throwing exceptions. Custom types of exceptions.')

#Unit testing basics
print('Unit testing basics')

