# Assignment 7: Odd or Even Checker Write a program that takes an integer input from the user
# and determines whether it's odd or even.
number = int(input("Enter the number you want to check: "))
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')