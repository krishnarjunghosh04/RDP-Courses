# Assignment 2: Temperature Conversion Write a program that converts temperature in Fahrenheit to Celsius.
# The formula is: Celsius = (Fahrenheit - 32) * 5/9.
# Take Fahrenheit from user.
temperature = float(input('Enter temperature: '))
celsius = round((temperature - 32) * 5/9,2)
print("Celsius temperature is",celsius)
