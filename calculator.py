import math

def get_numbers():
    """Helper function to collect multiple numbers from user."""
    nums = []
    while True:
        val = input("Enter a number (or type '=' to finish): ")
        if val.lower() == "=":
            break
        try:
            nums.append(float(val))
        except ValueError:
            print("Invalid input, please enter a number or '='.")
    return nums

def calculator():
    print("=== Python Calculator ===")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponent (^)")
    print("6. Root (√)")
    print("7. Trigonometry (sin, cos, tan)")
    print("8. Exit")

    while True:
        choice = input("\nChoose operation (1-8): ")

        if choice == "8":
            print("Exiting calculator... Goodbye!")
            break
        if choice in ["1", "2", "3", "4"]:
            nums = get_numbers()
            if len(nums) < 2:
                print("Please enter at least 2 numbers.")
                continue

            if choice == "1":  
                print("Result:", sum(nums))

            elif choice == "2":  
                result = nums[0]
                for n in nums[1:]:
                    result -= n
                print("Result:", result)

            elif choice == "3":
                result = 1
                for n in nums:
                    result *= n
                print("Result:", result)

            elif choice == "4":  
                result = nums[0]
                try:
                    for n in nums[1:]:
                        result /= n
                    print("Result:", result)
                except ZeroDivisionError:
                    print("Error: Division by zero!")

        elif choice == "5":
            a = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print("Result:", a ** b)

        elif choice == "6":
            number = float(input("Enter number: "))
            n = float(input("Enter root (e.g., 2 for square root, 3 for cube root): "))
            if n != 0:
                result = number ** (1/n)
                print("Result:", result)
            else:
                print("Error: Root cannot be zero!")

        elif choice == "7":
            func = input("Choose function (sin, cos, tan): ").lower()
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)  
OBOBOB            if func == "sin":
                print("Result:", math.sin(rad))
            elif func == "cos":
OBOBOB                print("Result:", math.cos(rad))
            elif func == "tan":
OBOBOB                print("Result:", math.tan(rad))
            else:
OBOBOB                print("Invalid trig function!")

        else:
            print("Invalid choice, try again!")

calculator()
