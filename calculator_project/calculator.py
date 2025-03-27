# Importing functions from operations.py
from operations import add, subtract, multiply, divide  

# Global variable to store the last result
last_result = None  

class Calculator:
    def run(self):
        global last_result  
        running = True  

        while running:
            print("\nBasic Calculator")

            # Using a for loop to print menu options
            menu = ["1. Add", "2. Subtract", "3. Multiply", "4. Divide", "5. Use Last Result", "6. Exit"]
            for option in menu:
                print(option)

            try:
                choice = int(input("Choose an operation (1-6): "))

                if choice == 6:
                    print("Exiting the calculator. Goodbye!")
                    running = False  
                    break
                
                elif choice == 5:
                    if not last_result:
                        print("No previous result available.")
                        continue
                    else:
                        print(f"Using last result: {last_result}")
                        a = last_result
                else:
                    if choice not in [1, 2, 3, 4]:  
                        print("Invalid choice. Please select a number between 1 and 6.")
                        continue
                    a = float(input("Enter first number: "))

                b = float(input("Enter second number: "))

                if a < 0 or b < 0:
                    print("Error: Both numbers must be non-negative.")
                    continue  

                # Using a generator with 'yield' to return the result
                def calculate(choice, a, b):
                    operations = {
                        1: ("Addition", lambda x, y: x + y),
                        2: ("Subtraction", lambda x, y: x - y),
                        3: ("Multiplication", lambda x, y: x * y),
                        4: ("Division", lambda x, y: x / y if y != 0 else "Error: Cannot divide by zero.")
                    }
                    if choice in operations:
                        operation_name, operation_func = operations[choice]
                        result = operation_func(a, b)
                        yield operation_name, result  # Using yield instead of return

                # Calling the generator function
                generator = calculate(choice, a, b)
                for operation_name, result in generator:
                    if isinstance(result, str):  
                        print(result)
                    else:
                        print(f"{operation_name} result: {result}")
                        last_result = result or 0  

                        # Using 'with' to log results in a file
                        with open("calculator_log.txt", "a") as log_file:
                            log_file.write(f"{operation_name}: {a} and {b} = {result}\n")

                # Delete a and b after use
                del a, b

            except ValueError as ve:
                print("Error:", ve)
                continue
            except Exception as e:
                print("Unexpected error:", e)
                continue


# Create an instance of Calculator and run it
calc = Calculator()
calc.run()

# Delete the calculator instance before exiting
del calc
print("Calculator instance deleted.")
