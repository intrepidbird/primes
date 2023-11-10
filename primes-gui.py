import tkinter as tk
from tkinter import messagebox

def is_prime(n):
    """
    Checks if a number is prime.

    Parameters:
    - n: int
        The number to be checked.

    Returns:
    - bool:
        True if the number is prime, False otherwise.
    """

    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

def generate_primes():
    """
    Generates prime numbers based on user input and displays them in a GUI.

    This function creates a GUI window with an input field and a button. The user can enter a number in the input field
    and click the button to generate prime numbers up to that number. The prime numbers are displayed in a message box.

    The function uses the is_prime function to check if a number is prime.

    Returns:
    - None
    """

    def on_generate():
        """
        Event handler for the generate button.

        This function is called when the generate button is clicked. It retrieves the user input from the input field,
        generates the prime numbers, and displays them in a message box.

        Returns:
        - None
        """

        # Get the user input from the input field
        input_value = input_field.get()

        try:
            # Convert the input value to an integer
            n = int(input_value)

            # Generate the prime numbers
            primes = [str(i) for i in range(2, n + 1) if is_prime(i)]

            # Display the prime numbers in a message box
            messagebox.showinfo("Prime Numbers", "\n".join(primes))
        except ValueError:
            # Display an error message if the input value is not a valid integer
            messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")

    # Create the GUI window
    window = tk.Tk()
    window.title("Prime Number Generator")

    # Create the input field
    input_field = tk.Entry(window)
    input_field.pack()

    # Create the generate button
    generate_button = tk.Button(window, text="Generate", command=on_generate)
    generate_button.pack()

    # Run the GUI event loop
    window.mainloop()

# Call the generate_primes function to start the prime number generator GUI
generate_primes()
