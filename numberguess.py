import random
a= random.randrange(10, 100)
#print("The number you should guess is ",a)
c=a/10
'''
if a%10==0:
    print("You have {} chances to guess the number".format(int(c+1)))
else:
    print("You have {} chances to guess the number".format(int(c-1)))
'''
print("lets began the game ")
print("You have {} chances to guess the number".format(int(c)))
for i in range(int(c)):
    z=int(input("enter a number : "))
    if z==a:
        print("You have guessed it right :-)")
        break
    elif(z>a):
        print("The number you have guessed is larger")
    elif(z<a):
        print("The number you have guessed is smaller ")
    else:
        print("Wrong number!!!! ")
print("The number you should guess is ",a)
print("Better luck next time ")
print("Thanks for playing with us")