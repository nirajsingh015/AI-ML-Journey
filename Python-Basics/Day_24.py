'''Python Tuples:

Tuples are ordered collection of data items. They store multiple items in a single 
variable. TUple items are seperated by commas and enclosed with in round brackest().
Tuples are unchangeable meaning we can not alter them after creation.'''

tuple1=(1,2,3,4,5,6)
tuple2 =("Red","Blue","Green")
print(tuple1)
print(tuple2)

#(1, 2, 3, 4, 5, 6)
#('Red', 'Blue', 'Green') #output

details=(1,"Niraj",1.2,)
print(details)
#(1, 'Niraj', 1.2)

tup=(1)
print(type(tup),tup)
#<class 'int'> 1
tup=(1,)
print(type(tup),tup)
#<class 'tuple'> (1,) if ther is only one element in tuple we should use, so that it is identified as tuple


'''Tuple Indexes:
Each item/element in atuple has its own unique index. THis index can be used to
access any particular item from the tuple. THe first item has index[0], second item
has index[1] and so on.'''
details=(1,"Niraj",1.2,)
print(details[0])
print(details[1])
print(details[2])

#1
#Niraj
#1.2

'''Positive Indexing: As we have seen that tuple items have index, as such we can access items using 
these indexes.'''
details=(1,"Niraj",1.2,)
print(details[0])
print(details[1])
print(details[2])

#1
#Niraj
#1.2
'''Negative Indexing: Similar to positive indexing neagtive indexing is also used to access items, but from 
the end of the tuple. THe last item has index[-1], the second last has indes[-2]
ans so on.'''
details=(1,"Niraj",1.2,)
#       -3    -2       -1
print(details[-1])
print(details[-2])
print(details[-3])
#output
#1
#Niraj
#1.2

'''Check for item:
we can check if a given item is present in the tuple. This is
done using the in keyword.'''

country=("India","UAE","England")
if "INDIA" in country:
    print("India is present.")
else:
    print("NO")

#India is present.
#NO if INDIA 