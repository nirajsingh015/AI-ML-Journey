'''List in Python
List are ordered colellection od data items.
They store mutltiple items in a single variable.
List items are seperated by commas and enclosed within square brackets[].
Lists ar changeable meaning we can alter them after creation.'''

l=[3,5,6]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
'''[3, 5, 6]
<class 'list'>
3
5
6
ouput'''
#we cad add string and bolleean data type in a list
marks=[1,"Niraj",True]
print(marks)
#[1, 'Niraj', True] output

''' List Index:
Each item/elements in a list has its own index. THis index can be used to access any particiular item from the list
The first item has index[0], second has index[1] and so on.'''

'''Accessing list items:
We can access list items by using it's index with the square barckt syntax[].
For example marks[0] will give "1" and so on.'''

'''Positive Indexing:
As we have seent that list items have index,as such we can access items using these indexes.'''
l=[3,5,6]
print(l)
print(type(l))
print(l[0])#3 output
print(l[1])#5 output
print(l[2])#6 output

'''Negative Indexing:
Similar to positive indexing, negstive indexing is also used to access
items, but from the end of the list. The last item has index[-1],second
last item has index[-2] and the third item has index[-3] and so on.'''

colors=["Red","Green","Blue","Orange","Yellow"]
# index  -5     -4      -3     -2        -1
print(colors[-1])
print(colors[-3])
print(colors[-5])
#to convert the negative in to postive we can convet by using len of marks
print(colors[len(colors)-3]) #Blue (output) same as negative will give
''' output:
Yellow
Blue
Red'''

'''check wheather an item is present in the list?
We can check if a given item i spresent in the list. This can be done
using "in" keyword'''
marks=[1,2,3,4,5,6,7,"niraj"]
if 7 in marks:
    print("yes")
else:
    print("No")
#yes (output)
#if "ni" in"niraj":#ouput will be yes and same thing applies in strings
if "niraj" in marks: #if we want to search a string in the list we need to use double quotes"""
    print("yes")
else:
    print("No")
#yes (output)

'''Range of Index:
You can print a ragne of list items by specifying where you wnat to start,
where do you want to end and if you want to skip elements in between the range.
Syntax:  listName[start :end: jump Index]
jumpindex is optional.'''

#this is same as string slicing
marks=[1,2,3,4,5,6,7,"niraj"]
print(marks)
print(marks[:])
#[1, 2, 3, 4, 5, 6, 7, 'niraj']output
print(marks[1:5])
#[2, 3, 4, 5] output
#jump index
print(marks[1:5:2])
#[2, 4]output

'''List Comprehension:
List comprehension are used for creating new lists fromother iterables liek lists,
tuples, dictionaries,sets, adn even in arrays and strings.
Syntax:
List= [Expression(item) for item in iterable if condtion]
Expression: It can be the item which is being iterated.
Condition: Condition checks if the item should be added to the new list or not.
'''
lst=[i for i in range(4)]
print(lst)
#[0, 1, 2, 3]output
#we can add only even numebr in the list with this
lst=[i for i in range(10) if i%2==0]
print(lst)
[0, 2, 4, 6, 8]
#Accepts items which have more than 4 cahracters
names=["Milo","sarah","Bruno","Anastansia","Rick"]
nameswith_0=[item for item in names if(len(item)>4)]
print(nameswith_0)
#['saraAh', 'Bruno', 'Anastansia'] output