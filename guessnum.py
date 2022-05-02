from gc import garbage
import random 
n=random.randint(1,9)

chance=5
guess = input("enter a number: ")
num=n
if chance >0 :
 if int(guess)==num:
    print("you won :)")
 elif int(guess)<num :
    print("guess a number higher than ",guess)
    chance-=1
 else :
    print("guess a number lower than ",guess)
    chance-=1
else :
    print("you lose :(")    


