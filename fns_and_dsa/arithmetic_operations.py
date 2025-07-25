# 1. Simple Calculator with Match Case


def perform_operation(num1: float, num2: float, operation: str) -> float:
    '''This performs arithmatic'''
    

    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1/num2

    return result