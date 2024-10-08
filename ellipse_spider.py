#Ellipse circumference 

def check_ellipse(x, y, a1, b1, a2, b2):
    """
    This method checks if the given point falls in between the ellipses.
        'x' -- given point x coordinate
        'y' -- given point y coordinate
        'a1' -- semi maJor axis of larger ellipse
        'b1' -- semi miNor axis of larger ellipse
        'a2' -- semi maJor axis of smaller ellipse
        'b1' -- semi miNor axis of smaller ellipse
    """
    if (x ** 2 / a1 ** 2 + y ** 2 / b1 ** 2 < 1) and (x ** 2 / a2 ** 2 + y ** 2 / b2 ** 2 > 1):
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()
    
    

