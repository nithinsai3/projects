
import time
hour  = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
seconds = int(time.strftime('%S'))
print("THE TIME IS ")
print(hour,end=":")
print(minute,end=":")
print(seconds)
if(hour >= 00 and hour<=12 ):
    print("GOOD MORNING ")
elif(hour>12 and hour<=16):
    print("GOOD AFTERNOON")
elif(hour>16 and hour<=19):
    print("GOOD EVENING")
else :
    print("GOOD NIGHT")