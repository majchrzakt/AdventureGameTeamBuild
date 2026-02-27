def validate_choice(prompt, choices):
    # Use quotes for strings and indentation for the function body
    print("--- Validate Choice ---")

    while True:
        c = input(prompt)
        if c in choices:
            return c
        else:
            print(f"Invalid input. Please choose from: {choices}")


def main():
    # Pass strings in quotes and lists in square brackets
    choice = validate_choice("Enter 1, 2, 3, or 4: ", ["1", "2", "3", "4"])
    print(f"You selected: {choice}")


# Call the main function to run the code
if __name__ == "__main__":
    main()