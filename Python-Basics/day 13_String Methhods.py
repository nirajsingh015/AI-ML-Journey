#String Methods
''' Python provides a set of built-in methods that we can use to alter and modidy the string.
String are immutable like we cannot chage once we created but we can definitely change by creating a copy of the string'''

'''upper():
The upper() method converts a string to uppercase.'''
str1="AbcdEfGhIj"
print(str1.upper())
#ABCDEFGHIJ(output)

'''lower():
The lower() method converts a string to lowercase.'''
print(str1)
#AbcdEfGhIj(output) so the actual string is immutable as we can see.
print(str1.lower())
#abcdefghij(output)

'''rstrip():
the rstrip() removes any trailling characters'''
str2 = "!!hello!!!"
print(str2.rstrip("!"))
#!!hello(output) it doesnot remove the leading characters

'''replace():
the replace() method replaces all occurances of a stringwith another string.'''

str3= "Niraj"
print(str3.replace("Niraj","Singh"))
#Singh(output) it will replace all occurances

'''Split():
The Split() method splits the given string at the specified instance and returns
the seperated strings as list items.'''
str4="Silver Spoon"
print(str4.split(" "))#split the string at the whitespace " ".
#['Silver', 'Spoon'](output)

''' capitalize():
The Capitalize() method turns only the first character of the string to uppercase
and the rest other character of the strings are turned to lowercase.
The string has no effect if the first character os already uppercazse.'''

blogheading="introduction to Python."
str5= blogheading.capitalize()#we can convert it first then we can print or we can directly convert.
print(str5) 
print(blogheading.capitalize())
#Introduction to python.(output)

'''center():
THe center()method aligns the string to the center as per the
parameters given by the user.'''

str6="Welcome to the conseole!"
print(str6.center(50))
#             Welcome to the conseole!    it added 50 space before the string.