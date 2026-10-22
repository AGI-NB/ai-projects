# username = input("Enter your username: ")
# password = input("Enter your password: ")

# while True:
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#     if username == '' or password == '':
#         print("Username and password cannot be empty. Please try again.")
#         continue  #继续循环
#     if username == "admin" and password == "password123":
#         print("Login successful!")
#         break  #终止循环
#     if username == "user" and password == "userpass":
#         print("Login successful!")
#         break  #终止循环
#     else:
#         print("Invalid username or password. Please try again.")
#         username = input("Enter your username: ")
#         password = input("Enter your password: ")

import random
number = random.randint(1, 100)  #生成随机数
while True:
    guess = int(input('Guess a number between 1 and 100:'))  #接收猜的数字
    if guess < number:
        print('Too low!')
    elif guess > number:
        print('Too high!')
    else:
        print('Congratulations! You guessed the number.')
        break