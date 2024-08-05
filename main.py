from art import logo

def add(a, b):
    return a + b
def substract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": substract,
    "*": multiply, 
    "/": divide,
}

def calculator():
    print(logo)
    
    a = float(input("What's the first number? "))
    start_again = True

    while start_again:
        for operation in operations:
            print(operation)
            
        operation_symbol = input("Pick an operation: ")
        b = float(input("What's the next number? "))
    
        calculation_function = operations[operation_symbol]
        answer = calculation_function(a, b)
    
        print(f"{a} {operation_symbol} {b} = {answer}")
        
        start_again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        
        if start_again == "y":
            a = answer
        else:
            start_again = False
            calculator()
            
calculator()