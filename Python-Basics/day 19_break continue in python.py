'''Break Statements
The Break statement enables a program to skip over a part of the code. A break statement
terminates the very loop it lies within.'''
#IT WILL SKIP THE  LOOP IF THE BREAK IS EXECUTED
for i in range(1, 101,1):
    print(i,end=" ")
    if(i==50):
        break
    else:
        print("missisipi")
print("thank you")
#IT WILL SKIP THE ITERATION IF THE CONDITION IS MATCHED
'''Continue Statement:
THe continue statement skips the rest of the loop
statements and causes the next iteration to occur..'''

for i in [2,3,4,5,6,7,8,0]:
    if(i%2!=0):
        continue
    print(i)

'''
2
4
6
8
0'''#(output)