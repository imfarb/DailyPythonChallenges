import math
from math_utils import * 
while True:
    
    print("""
    Select Operation:
    0. Exit
    1. Addition
    2. Subtraction
    3. Multiply
    4. Divide
    5. Power
    6. Sine
    7. Cosine
    8. Tangent
    9. Cotangent
    10. Natural Logarithm
    11. Logarithm Base 10
    12. Logarithm with Custom Base
    """)

    operation = {
        1 : add,
        2 : subtract,
        3 : multiply,
        4 : divide,
    }
    
    trig_functions = {
        6 : sine,
        7 : cosine,
        8 : tangent,
        9 : cotangent,
    }
    
    log_function = {
        10 : natural_log,
        11 : log_base_10,
        12 : log_custom_base,
    }
    
    
    choice = int(input("Enter your choice : "))
    if choice == 0:
        print("Exiting program. Goodbye!")
        break
    elif choice in operation:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Invalid input. Please enter valid numbers.")

        result = operation[choice](num1, num2)

        print(f"The result of your calculation is: {result:.2f}")
        
    elif choice == 5:
        try:
            num = float(input("Enter first number: "))
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
        base = float(input("Enter base number to power: "))

        result = power(num, base)
        print(f"The result of your calculation is: {result:.2f}")
      
      
    
    elif choice in trig_functions:
        try:
            angle = float(input("Enter angle: "))
        except ValueError:
            print("Error: Invalid input. Please enter a valid angle.")
        angle_rad = angle_to_radians(angle)
        
        result = trig_functions[choice](angle_rad)
        
        print(f"The result of your calculation is: {result:.2f}")

    
    elif choice in log_function:
        try:
            number = float(input("Enter number: "))
            if choice == 12:
                base = float(input("Enter base: "))
                result = log_function[choice](number, base)
                print(f"The result of your calculation is: {result:.2f}")
                continue
            result = log_function[choice](number)
            print(f"The result of your calculation is: {result:.2f}")
            
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
    
    else:
        print("Invalid choice. Please try again.")
        break

        

    