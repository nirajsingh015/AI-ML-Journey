#typecasting in python
""" The conversion of one data type into the other datat type is known as type
casting or type conversion in python"""
""" Python supports a wide varitey of functions or methods like: int(), float(),
str(),hex(), oct(), ord(), set(), tuple(), list(), dict(), etc. for type casting in pyhton """

#a="1"
a="1"
#B=2
b="2"
#IF WE ADD A+B WE WILL GET 12 
print(a+b)# ans is 12
#here we are typecasting and converting it the str into int datatype
print(int(a)+int(b))#ans= 3


#two types of TYpecasting:
""" 1. Explicit Conversion( explicit type casr=ting in pyhton)
    2. Implicit Conversion(Implicit type casting in python)"""

""" EXPLICIT CONVERSION: The conversion of one data type into another data type, done via
developer or programmer's intervention or manually as per the requirment, is known as implicit
type conversion. It can be achieved with the  help of python's built in type conversion functions
such s int(),float(), hex(),Str()etc.
"""
"""Example: print(int(a)+int(b))#ans= 3"""

string ="15"
number=7
string_number= int(string)#throws an error if the 
#string is not a valid int
sum= number+string_number
print("the sum of both number is:",sum)
#output is 22

#Implicit type casting
""" Data types in Python do not have the same level.i.e odering
of data types is not same in python. some of the data have 
high-order, adn some have lower order. While performing any operations
on variables with different data types in Python, one of the
variable's data type will be changed ti the higher datat type.
According to the level, one data type is converted into other by python interpreter itself(autoamtically).
this is called, implicit typecasting in python"""

"""Python converts a smaller data type to a higher data type
to prevent data loss."""

#Implicit typecasting
c=1.9
print(type(c))
d=8
print(type(d))
print(c+d)
print(type(c+d))
#answer will be 9.9
#here the data type is automatically covnvertred in to higher data
#type which is flot to save data loss
