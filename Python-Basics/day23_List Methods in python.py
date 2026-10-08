#List Methods:-
'''List  in Python'''
'''In Python List is a built-in, ordered and mutable collection used to store multiple
items in a single variable.''' 

'''List Methods:
list.sort():
This method sorts list in ascending order. The original list is updated.'''
colors =["violet","blue", "green", "indigo",]
colors.sort()
print(colors)
#['blue', 'green', 'indigo', 'violet'](output)

'''We can add elemts in list using append method.'''
colors.append("red")
print(colors)
#['blue', 'green', 'indigo', 'violet', 'red']

num=[9,2,1,4,5,7,8,4]
num.sort()
print(num)
#[1, 2, 4, 4, 5, 7, 8, 9](output)

'''reverse() method:
This method reverse the order of the list.
The reverse method is set to false by default.'''
num=[9,2,1,4,5,7,8,4]
num.reverse()
print(num)
 #[4, 8, 7, 5, 4, 1, 2, 9] (output)

'''index method:
This method returns the index of the first occurance of the list items.'''
num=[9,2,1,4,5,7,8,4]
print(num.index(4))
#3(output)

'''count method:
Returns the count of the number of items with the given value.'''
num=[9,2,1,4,5,7,8,4]
print(num.count(4))
#2(output)

'''copy method:
This method return copy of the list , This can be done to perform
operations on the list without modifying the original list,'''
colors =["violet","blue", "green", "indigo",]
newlist=colors.copy()
print(colors)
print(newlist)
#['violet', 'blue', 'green', 'indigo']
#['violet', 'blue', 'green', 'indigo']  (output)

'''insert method:
This method inserts and item at the given index. User has to 
specify index and the item to be inserted within the insert mehtod.'''
colors =["violet","blue", "green", "indigo",]
print(colors)
colors.insert(1, "red")
print(colors)
#['violet', 'blue', 'green', 'indigo']
#['violet', 'red', 'blue', 'green', 'indigo'] (output)

'''extend method:
This method adds an entire list or any other collections datatype
(set, tuple, dictonay)to the existing list.'''
colors =["violet","blue", "green", "indigo",]
colors2=["red", "yellow"]
colors.extend(colors2)
print(colors)
#['violet', 'blue', 'green', 'indigo', 'red', 'yellow'](output)

'''Concatenating two lists:
You can concatenate two lists to join two list'''
colors =["violet","blue", "green", "indigo",]
colors2=["red", "yellow"]
print(colors+colors2)
#['violet', 'blue', 'green', 'indigo', 'red', 'yellow'](output)