#String Slicing
'''String Slicing and Operations on String

We can fin the length of a string using len() function'''

fruit= "mango"
len1= len(fruit)
print("mango is a", len1,'letter word.')

# print(fruit[0:4]) # WE USE SQUARE BARKETS FOR SLICING
# print(fruit[1:5])#including 1 but not 5
# print(fruit[:5])
# print(fruit[:])#IT AUTOMATICALLY FETCHES THE LENGTH
# print(fruit[0:-3])#NEGATIVE SLICING HER - 3 IS INTERPRETED AS LEN OF FRUIT-3 = 2 WHICH IS 0 AND 1 INDEX
print(fruit[-1:len(fruit)-3])
print(fruit[-3:-1]) #output is ng 
#this is because
print(fruit[-4:-2])# here mango is 5 letter so
# pyhton will subtract 5 -4=1 and 5 -2  i s3
#so it will print  m=0,a=1, n=2,g=3,o=4 
# the output will be 'an'.

