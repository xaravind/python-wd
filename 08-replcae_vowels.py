#!/usr/bin/env python
# Author: Aravind Basava
# Email : aravind@gmail.com
# Take the input of words 
# script to replace x with vowels in a word

vowels= 'aeiouAEIOU'
inp_str=input("Enter the string: ")
inp_list= list(inp_str)

for idx in range(len(inp_list)):
    if inp_list[idx] in vowels:
        inp_list[idx] = 'x'

outp_string=''.join(inp_list)
print(f'The processed string is: {outp_string}')
