def calculator():
    while True:
        try:
            # Get user input
            cal = input("\nEnter your calculation (or type 'exit' to quit): ")

            # Exit condition
            if cal.lower() == 'exit':
                print("Calculator exited. Goodbye!")
                break

            # Evaluate the mathematical expression safely
            result = eval(cal, {"__builtins__": {}}, {})

            # Display the result
            print("Result:", result)

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception as e:
            print("Error: Invalid input.", e)

# Run the calculator
calculator()
