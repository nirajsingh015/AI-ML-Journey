#calculator
while 1>0:
    num1= float(input('Enter First number:'))
    operator =input("Enter operator(+,-,*,/):")
    num2= float(input("Enter Second number:"))
    if operator =="+":
        print("Result =",num1 + num2)
    elif operator =="-":
        print("Result =",num1 - num2)
    elif operator =="*":
        print("Result =",num1 * num2)
    elif operator =="/":
        if num1!=0:
            print("Result =",num1 / num2)
        else:
            print("Erroe! Division by Zero is not allowed.")
    else:
        print("Invalid Operator!")




