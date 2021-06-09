import math
import input_reader


def quadratic_equation_solver():
    print("Welcome to the Quadratic Equation Solver\n")
    a, b, c = get_coefficients()
    res = find_roots(a, b, c)
    print_result(res)


def get_coefficients():
    print("Please enter the coefficients a, b, and c for the equation.")
    a = input_reader.get_number_input("Please enter a value for a: ")
    b = input_reader.get_number_input("Please enter a value for b: ")
    c = input_reader.get_number_input("Please enter a value for c: ")
    return a, b, c


def find_roots(a, b, c):
    if a != 0:
        # Solve the full quadratic formula/equation.
        d = b * b - 4 * a * c
        #print(d)
        if d > 0:
            x = (-b + math.sqrt(d)) / (2 * a)
            y = (-b - math.sqrt(d)) / (2 * a)
            return (2, [x, y])
        elif d == 0:
            x = -b/(2 * a)
            return (1, [x])
        else:
            return (0, [])
    else:
        # Solve the linear formula/equation.   
        if b != 0:
            x = -c / b
            return (1, [x])       
        else:
            if c == 0:
                return (3, [])
            else:
                return (0, [])

##def find_roots_alternative(a, b, c):
##    if a != 0:
##        # Solve the full quadratic formula/equation.
##        d = b * b - 4 * a * c
##        #print(d)
##        if d > 0:
##            x = (-b + math.sqrt(d)) / (2 * a)
##            y = (-b - math.sqrt(d)) / (2 * a)
##            return (2, [x, y])
##        elif d == 0:
##            x = -b/(2 * a)
##            return (1, [x])
##        else:
##            return (0, [])
##    elif b != 0:
##        x = -c / b
##        return (1, [x])       
##    elif c == 0:
##        return (3, [])
##    else:
##        return (0, [])

    
def print_result(result):
    if result[0] == 0:
        print("No solution.")
    elif result[0] == 1:
        print(f"The solution is {result[1][0]}")
    elif result[0] == 2:
        print(f"The solutions are {result[1][0]} and {result[1][1]}")
    else:
        print("There are infinite many solutions.")

if __name__ == "__main__":
    quadratic_equation_solver()
