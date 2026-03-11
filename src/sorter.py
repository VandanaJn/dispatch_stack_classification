
VOL_THRESHOLD = 1000000
DIM_THRSHOLD = 150
MASS_THRSHOLD = 20
STACK_REJECTED = "REJECTED"
STACK_SPECIAL = "SPECIAL"
STACK_STANDARD = "STANDARD"

def is_bulky(width: float, height: float, length: float)-> bool:
    """
    Check if a package is bulky based on volume or dimensions.
    A package is bulky if volume >= 1,000,000 or any dimension >= 150.
    """
    volume=width*height*length
    if volume>=VOL_THRESHOLD:
        return True
    if width>=DIM_THRSHOLD or height>=DIM_THRSHOLD or length>=DIM_THRSHOLD:
        return True
    return False

def is_heavy(mass: float)-> bool:
    """
    Check if a package is heavy based on mass threshold (>= 20).
    """
    return mass>=MASS_THRSHOLD

def sort(width: float, height: float, length: float, mass: float)-> str:
    """
    Sort a package into one of three category stacks: REJECTED, SPECIAL, or STANDARD.
    Returns REJECTED if both bulky and heavy, SPECIAL if either bulky or heavy, else STANDARD.
    """
    bulky=is_bulky(width,height,length)
    heavy=is_heavy(mass)
    if bulky and heavy:
        return STACK_REJECTED
    if bulky or heavy:
        return STACK_SPECIAL
    return STACK_STANDARD
    