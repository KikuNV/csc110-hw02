# ------------------------------------------------------
#        Name: (KIKU NAGAI-VELASQUEZ)
#       Peers: (NONE)
#  References: (NONE)
# ------------------------------------------------------

# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    """this gives two functions"""
    x = int(input("give me x: "))
    y= int(input("give me y: "))
    y=int(y)
    return x, y 
    
        
# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    """multiplies a and b, then adds a and b"""
    mult_ab = a*b
    print("mult result:", mult_ab)
    add_ab = a + b
    print("add result:", add_ab)

    return mult_ab/add_ab

      

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
   
    print("****************")
    print("RESULTS:")
    print("first number:", a)
    print("second number:", b)
    print("multadd result:", ab_multadd)
    print("================")
    
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below


def main ():
    """the func stores two variables from read_two_ints"""
    x, y = read_two_ints()
    
    """the function is given xy and returns the multadd of them"""
    xy_multadd = compute_multadd(x,y)
    
    """print_fancy func prints formatting for our x, y and multadd"""
    print_fancy(x, y, xy_multadd)
    

    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
    
    
"""- [x] you added your name to the top comments of the python file
- [x] runs without syntax errors (or -50%)
- [x] adds a few small but informative comments (or -5%)
- [x] adds docstrings to each function (or -5%)
- [x] Passes all tests (or lose 15% per missed test). If you do not pass all tests, do not check this box
- [x] You checked the correct boxes"""
