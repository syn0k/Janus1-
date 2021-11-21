import math
#Error handling basic
print('Error handling basic: Example: 1')

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as ex:
        print(f'On error occured: {ex}')
    except:
        print('Error occured')

print('Error handling basic: Example: 2')
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

print('Example: 3')


def enter_the_number():
    while True:
        try:
            reply = int(input('Enter the number'))
            return reply
        except:
            print('Not a number! Try agein')
            continue


enter_the_number()

print('Example: 4')

# Exception error
class InvalidTriangleError(Exception):
    """Raised when a triangle has invalid sides"""

def calc_square(ab, ac, ad):
    if ab <= 0 or ac <= 0 or ad <= 0:
        #raise ValueError('One of the sides is less or equal to 0.')
        raise InvalidTriangleError('One of the sides is less or equal to 0.')

    p = (ab + ac + ad) / 2
    s = math.sqrt(p *(p-ab) * (p-ac) * (p-ad))

    return s

printsq = calc_square(-10,12,12)
print(printsq)

#Unit testing basics
print('Unit testing basics')

