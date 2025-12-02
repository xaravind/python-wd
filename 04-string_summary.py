#!/usr/bin/env python
# Author: Aravind Basava
# Email : aravind@gmail.com
# Given a string (input from the user)
# print - Number of Characters, number of Words

# Taking input from the user
inp_str = input("Enter the string: ")
 
# Get the number of characters
number_of_chars = len(inp_str)
 
# Get the number of words
number_of_words = len(inp_str.split())
 
# print the number of vowels
vowels = 'aeiou'
inp_str = inp_str.lower()
 
number_of_vowels = 0
# for i in range(len(inp_str)):
#     if inp_str[i] in vowels:
#         number_of_vowels += 1
 
for chr in inp_str:
    if chr in vowels:
        number_of_vowels += 1
 
print(f"Number of characters in given string is: {number_of_chars}")
print(f"Number of words in given string is: {number_of_words}")
print(f"Number of vowels in given string is: {number_of_vowels}")
 