#Comments and escape sequence and print statements

# this is single comment line(# this is used to declare as comment)
print("hello how 'are' you \n and you ar going to learn esacape sequence using dash n")

#multiline comments
"""this is a  multi line comment using triple and double quotes
hello
world
python
"""
#print statements
# ~is used to seperate  default is space
#end is used to specify what to print at the end
print("hey", 6, 7, 8,sep="~", end="009\n")
print("nirajj")

#Variables in python
a= 1232425426
print(a)
b="Niraj"
print(b)
c=True #boolean datat ype
d=None #null type value
a1=10
print(a + a1)
print("the type of a is",type(a))
print("the type of a is",type(b))
print("the type of a is",type(c))
print("the type of a is",type(d))

#built in data types
# int float comples
#boolean datat types
e=complex(8 , 2)
print(e)
#text data str"HEllo world" "python programming"

#sequenced Data list, tuble

#list is an ordered collection of data with elements
#seperated by commas and encoded with square barcakerts. list are mutuable acn can be modified\n
#after creation
list1= [[8,3.3],['Apple','banana']]
print(list1)


#tuple
#tuple is an ordered collection of data with elemets sepearted by 
#commass, and enclosed within parentheses().
#tuples are immutable and cannot be modifed after creation.
tuple1 =(8, 2,4,(4,-5),('apple', 'banana'))
print(tuple1)

#mapped data :dict
#a dictionary is an unordered collection of data
#containing a key value pair. the key value pair are
#ENCLOSED with curly brackets{}
dict1 ={"name":"niraj","age":20,"canvote":True}
print(dict1)

#everthing in python is an object!!