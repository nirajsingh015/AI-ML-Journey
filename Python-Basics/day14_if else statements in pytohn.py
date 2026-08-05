'''If-else Statements
Sometimes the programmer needs to check the evalutaion of certain
expresssion(s), whether the expression(s) to True or False. If the expression evaluates
to False, then the program execution follows a different path
than it would have if the expression had evaluated to True.

Based on this, the conditional statements are further into
following types.

if
if-else
if-else-elif
nested if-else-elif

An if......else statement evaluates like this:
if the expression evauates True:
    executes the block of code inside if statement. After execution return to
    the code out of the else block
if the expression evaluates False:
    execute.'''


'''Conditional operators in python:
>, <, >=, <=, ==, != '''

a= int(input("Enter your age: "))
print("Your age is:",a)
if(a>18):
    print("you can drive") 
else:
    print("You can't drive")

'''if-elif-else '''

num=int(input("Enter the value of num: "))
if(num<0):
    print("Number is negative")
elif(num==0):
    print("Number is zero. ")
else:
    print("Number is positive")

#Enter the value of num: -11
# Number is negative(output)
# Enter the value of num: 6
# Number is positive
# Enter the value of num: 0
# Number is zero. 