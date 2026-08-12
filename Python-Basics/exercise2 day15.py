import time
timestamp= time.strftime("%H,%M,%S")
print(timestamp)
H= int(time.strftime("%H"))
print(timestamp)
if(5<=H<=12):
    print("Good Morning!")
elif(12 == H<=17):
    print("Good Afternoon!")
elif(17== H <21):
    print("Good Evening!")
else:
    print("Good Night!")
