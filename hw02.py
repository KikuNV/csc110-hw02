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
    """Task 1.2 stores two variables from read_two_ints"""
    x, y = read_two_ints()
    xy_multadd = compute_multadd(x,y)
    print_fancy(x, y, xy_multadd)
    
    # ADD a Docstring for this function
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y

    # TODO: add your call instead of this line

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd

    # TODO: add your call instead of this line

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    # TODO: add your call instead of this line


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
    
    
"""- [x] you added your name to the top comments of the python file
- [ ] runs without syntax errors (or -50%)
- [x] adds a few small but informative comments (or -5%)
- [x] adds docstrings to each function (or -5%)
- [ ] Passes all tests (or lose 15% per missed test). If you do not pass all tests, do not check this box
- [x] You checked the correct boxes"""
