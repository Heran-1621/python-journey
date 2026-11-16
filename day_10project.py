#CALCULATOR
#ADD
def add(n1, n2):
    return n1+n2

#SUBTRACT
def subtract(n1, n2):
    return n1-n2
#MULTIPLY
def multiply(n1, n2):
    return n1*n2
#DIVIDE
def divide(n1, n2):
    if n2!=0:
        return n1/n2
    return "invalid input"
operations={
    "+": add,
    "*":multiply,
    "-": subtract,
    "/":divide
}
def calculator():
    num1=float(input("What is the first number: "))
    for operator in operations:
        print(operator)
    should_continue=True   




    while should_continue:

        operation_symbol=input("Pick an operation")
        next_num=float(input("What is the next number: "))
        calculaton_function= operations[operation_symbol]
        answer=calculaton_function(num1,next_num)
        print(f"{num1} {operation_symbol} {next_num}={answer}")
        
        continue_working=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.:  ")

        if continue_working=="y":
            num1=answer
        else:
            should_continue=False
            calculator()
        
    


 
