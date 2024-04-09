from random import *
u_pwd = input("Enter a password : ")
pwd=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

pw=""
while(pw!=u_pwd):
    pw=""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0,25)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print("Cracking Password...Please wait")
print("Your Password Is :",pw)        
