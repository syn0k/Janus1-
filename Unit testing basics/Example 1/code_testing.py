from math import pi

def circle_area(radius):
    if type(radius) not in [int, float]:
        raise ValueError("Radius must be non-negativ real number only")
    if radius < 0:
        raise ValueError("Radius can't be negative")
    return pi*radius**2

