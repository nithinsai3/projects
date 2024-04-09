import random
letters = ['a','b', 'c', 'd', 'e','f','g','h','i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v','w','z','x','y','z']
numbers =['1','2','3','4','5','6','7','8','9', '0']
symbols = ['~','!','@','#','$','%','^','&','*']
character = int(input ("enter the no of letter :"))
num = int(input("enter the no of numbers : "))
symb = int(input("Enter the number of symbols: "))
password_list = []
for i in range(1,character+1):
    char = random.choice(letters)
    password_list += char
#print("Password with letters is ",password_list)
for j in range (1, num+1):
    num_random =random.choice(numbers)
    password_list += num_random
#print("Password with numbers is ",password)
for k in range(1,symb+1):
    symbols_random=random.choice(symbols)
    password_list += symbols_random
#print("password is ",password_list)
random.shuffle(password_list)
password=''
#print(password_list)
for chara in password_list:
    password+=chara
print(password)



