"""In python anything enclolses between single or double quotation marks is considered a string.
A string is a sequence or array of textual data.
Strings are used when working with Unicode characters. """

name= "niraj"
name1='singh'
print("hello "+ name +""+name1)
print("hello ",name,name1)

#multiple line string
message ='hello how are you!'
print(message)

#if we want to  print multiple line  then we use '''
message1='''hello
how are you!
are you doing good '''
 
print(message1)

#Accessing Charecters of a string
'''In python, String is like an array of cahracters. 
we can access parts of a string by using its index which starts from 0.
Square brackets can be used to access elements of the string.'''
print(name[0])
print(name[1])

#looping through the string
for character in name:
    print(character)
