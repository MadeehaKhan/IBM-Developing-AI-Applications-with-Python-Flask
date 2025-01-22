import math

def area_of_rectangle(length, breadth):
    """
    This function returns the area of a given rectangle.
    The area is calculated as the product of the rectangle's length and breadth.
    """
    # Calculate the area by taking length and breadth as input and returning the area of a rectangle
    # We multiply the length by the breadth to obtain the area of the rectangle

    return length*breadth 

def area_of_circle(radius):
    """
    This function returns the area of a given circle.
    The area is calculated using the pi constant and multiplying it by the square of the circle's radius.
    """
    # Calculate the area by taking the radius as input and using the math.pi constant from Python's math library and returning the area of the circle
    # math.pi gives the value of pi which is required to calculate the area of a circle
    # radius**2 gives us the square of the radius which is required to calculate the area of the circle
    # We multiply pi and the square of the radius to obtain the area of the circle
    square_radius = radius**2

    return math.pi*square_radius