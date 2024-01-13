import random

#create an variable from where your password will get data to generate passowrd
char = "1234567890!@#$%^&*abcdefghijklmnopqrstuvwxyzABCDEFGHIJLMNOPQRSTUVWXYZ"

#create a variable to store password
password = ""

#now create an variable to decide the length of your password
length = int(input("Enter the length of your password: "))

#to generate random password create an loop
for i in range(length):
    password=password+random.choice(char)

#print the password
print(password)

#THANK YOU