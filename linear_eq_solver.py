import time
import input_reader

def linear_equation_solver():

    print("Welcome to the Linear Equation Solver\n")
    time.sleep(1)

    while True:

        print("Please enter a number for the coefficients m and b in the equation m*x+b=0")

        m = input_reader.get_number_input("Enter a value for m: ")
        b = input_reader.get_number_input("Enter a value for b: ")

        if m == 0:
            print("No solution.")
        else:
            solution = -b/m
            print(f"The solution is = {solution}")

        print("\nPress q for quit.")
        q = input()

        if q == "q" or q == "Q":
            break


if __name__ == "__main__":
    linear_equation_solver()
