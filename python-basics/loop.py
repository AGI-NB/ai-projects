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

# from ast import Continue
# import random
# number = random.randint(1, 100)  #生成随机数
# while True:
#     guess = int(input('Guess a number between 1 and 100:'))  #接收猜的数字
#     if guess < number:
#         print('Too low!')
#     elif guess > number:
#         print('Too high!')
#     else:
#         print('Congratulations! You guessed the number.')
#         break

#优化
import random

number = random.randint(1, 100)
attempts = 0 # Add a counter

print("I have thought of a number between 1 and 100.")

while True:
    try:
        guess = int(input('Guess a number between 1 and 100: '))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
        
    # Range check
    if guess < 1 or guess > 100:
        print("The number must be between 1 and 100!")
        continue
        
    attempts += 1 # Add 1 for every valid guess

    if guess < number:
        print('Too low!')
    elif guess > number:
        print('Too high!')
    else:
        # Output the number of guesses
        print(f'Congratulations! You guessed the number in {attempts} tries.')
        break