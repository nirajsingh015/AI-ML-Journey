'''Function Arguments and return Statements.

There are four types of a arguments that we can provide in a functions:

1. Default Arguments
2. Keyword Arguments
3. Variable Length Arguments
4. Required Arguments

Defualt arguments:
WE can provide a default value while creating a funtion. This way the 
function assumes a default value even if a value is not provided int the
functions call for that argument.
'''

def average(a=9, b=1):#defualt value will be used if nothing is provided while calling the fuction
    print("The average is",(a+b)/2)
average(b=9)# here it will take default value and return output

'''Keyword arguments: we can prvoide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name,
Hence, the order in which the argument are passed'''
def name(fname, mname, ename):
    print("Hello!,", fname, mname, ename)

name(ename="Singh", mname="Kumar", fname="Niraj") #it does not matter in which order we are passing order it will know using the parametnet name.
#Hello!, Niraj Kumar Singh(output)

'''Required arguments: In case we don't pass the argument with a key = value syntax,
then it is necessary to pass the arguments in the correct positional order and the number of argumnets 
passed should match the actual function defination.'''

def name(fname, mname, ename):
    print("Hello!,", fname, mname, ename)

#name("Singh", "niraj")
#TypeError: name() missing 1 required positional argument: 'ename'(output)

name("Niraj", "Kumar", "Singh")
#Hello!, Niraj Kumar Singh(output)


'''Variable Length arguments:
Sometimes we may need to pass more arguments than those
defined in teh actual function. This can be done using variable-length
arguments.
There are two ways to achieve this:

1. Arbitary Arguments:
While creating a function pass a * before the parameter name while
defining the function, The funtion access the arguments by processing them in the
format of tuple.'''

def name(*name):
    print("Hello", name[0], name[1], name[2])
name("Niraj", "Kumar", "Singh")
#output Hello Niraj Kumar Singh>

'''2. Keyword Arbitray arguments: while creating a function, pass a ** before the pareameter name
while defining the function. The funtion access the arguments by
processing them iin the form of dictonary.'''

def name(**name):
    print("Hello", name["fname"], name["mname"], name["ename"])
name(mname="kumar", fname="Niraj", ename="singh")
#Hello Niraj kumar singh(output)


'''Return Statement:
The return statement is used to return the value  of the 
expression back to the calling function.'''
def multiply(a, b):
    return a*b  # send the calculated result back
#the calculated value 10 is sent back and saved into result.
result= multiply(5,2)
print(result+ 10) #output 20