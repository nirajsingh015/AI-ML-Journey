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
# we can also provide padding character.It will full the rest of the 
#fill characters provided by the user.
print(str6.center(50,","))
#,,,,,,,,,,,,,Welcome to the conseole!,,,,,,,,,,,,,(output)

'''count():
The count() method returns the number of times the given value
has occured within the given string'''

str7="aabcccdegfffhij"
print(str7.count("a"))
#2(ouput)

'''endswith():
The endswith()method checks if the string ends with a given value.
if yes then return true, else return false.'''

str8="Welcome to console log!!!"
print(str8.endswith("!!!"))
#We can even check fo value on between the string by providing the start and end  index positions.

print(str8.endswith("to",4,10))


'''find():
The find() method searches for the first occurances of the given value 
and returns the index where it is present. It give value is absent from
the string then return -1.'''
str8="Welcome to console log!!!"
print(str8.find("to"))
#8(output)
print(str8.find("the"))
#-1(output)

'''Index():
The index() method searches for the first occurances of the given value
and returns the index where it is present. If the given value is absent from
the string then raise an exception.'''
str8="Welcome to console log!!!"
print(str8.index("console"))
#11(output)
#if the value is not present then is retuns error.
print(str8.index("the"))
#ValueError: substring not found(output)

'''isalnum():
The alnum() method returns true if the entire string only contains
of A-Z,a-z,0-9. If any other characters or punctuations are
present, then it returns False.'''
str9="HelloWorld123"
print(str9.isalnum())
#True(output)
str10="Hello123.,"
print(str10.isalnum())
#False(output)

'''isalphs():
The isalpha() method returns true if the entire string only contains
of A-Z,a-z,. If any other characters or punctuations or number(0-9)are
present, then it returns False.'''
str9="HelloWorld"
print(str9.isalpha())
#True(output)
str10="Hello123"
print(str10.isalpha())
#False(output)

'''islower():
The is lower() method returns True if all the characters is the string
are lower case,else it returns false.'''
str9="HelloWorld"
print(str9.islower())
#False(output)
str11="helloworld"
print(str11.islower())
#True(output)

'''is printable():
THe is printable() methid reruns True if all the values within the given
string are printable, if not, then it returns False.'''
str12="Hello world1"
print(str12.isprintable())
#True(output)
str12="Hello world1\n" #\n is not visible so it retuns false

print(str12.isprintable())
#False(output)

'''isspace():
The isspace() method returns true only and only if the strings
contains white spaces, else returns false.'''
str13="      "#using space bar
print(str13.isspace())
str13="         "#using tab
print(str13.isspace())
#True(output)

'''istitle():
The istitle() method returns True only if teh first letter of each word of the
string is capitalized, else it returns False.'''
str13="World Health Organization"
print(str13.istitle())
#True(output)
str13="World health organization"
print(str13.istitle())
#False(output)

'''isupper():
The isupper() method retuns True if all the characters in the strings are
upper case, else it returns False. '''
str13="WORLD HEALTH ORG"
print(str13.isupper())
#True(output)

'''startswith():
The startswith() method checks if the string starts with a given value. If yes
the returns True, else False.'''
str13="WORLD HEALTH ORG"
print(str13.startswith("W"))
#True(output)

'''swapcase():
The swapcase() method chnages the characters of the string. upper case 
are converted to lower case and lower case to upper case.'''
str13="WORLD hEALTH ORG"
print(str13.swapcase())
#world Health org(output)

'''title():
The title() method capitalizes each letter of the word within the string'''

str14="welcome to the console!"
print(str14.title())
#Welcome To The Console!(output)