
def get_number_input(prompt_message):
    input_str = ""
    while True:
        input_str = input(prompt_message)
        try:
            return float(input_str)
        except ValueError:
            print(f"'{input_str}' is not a number! Try again.")
            

if __name__ == "__main__":
    number = get_number_input("Enter a number: ")
    print(f"Got: {number}")
