#!/usr/bin/env python
# Author: Aravind Basava
# Email : aravind@gmail.com
# Example: The apple costs Rs.12 and oranges costs Rs.50
# Ouput: 12, 50

inp_str = input("Enter the string: ")

number="0123456789"

for i in inp_str:
    if i in number:
        print(i)
