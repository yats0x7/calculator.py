print("---SIMPLE CALCULATOR---")
def calc():
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    op = input("enter a operation (+, -, *, /, %, //, **): ")
    if op == "+":
        return(a+b)
    elif op == "-":
        return(a-b)
    elif op == "*":
        return(a*b)
    elif  op == "/":
        if b == 0:
            return("Error: Division by zero")
        else:
            return(a/b)
    
    elif op == "%":
        if b == 0:
            return("Error: Division by zero")
        else:
            return(a%b)
    elif op == "//":
        if b == 0:
            return("Error: Division by zero")
        else:
            return(a//b)
    elif op == "**":
        return(a**b)
    else:
        return("Invalid operation")
    
print(calc())