"""
Write a Python program to find and print all numbers divisible by 7 between 1 and 300. Use a for loop and the modulus operator (%).
"""
for i in range(7, 300, 7):
    if i % 1 == 7:
        continue
    print(i)