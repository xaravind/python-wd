#!/usr/bin/env python
# Author: Aravind Basava
# Email : aravind@gmail.com
# Take the input of list of numbers separated by spaces

# numbers: str=input("Enter list of numbers sepated by spaces")
# num_in_list=[]
# numbers=numbers.split()
# for num in numbers:
#     num_in_list.append(int(num))
# print(num_in_list)


numbers = list(map(int,input("Enter list of numbers seperated by spaces: " ).split()))

length_of_list = len(numbers)

numbers.sort()

print(f"second loswest is : {numbers[1]}")
print(f"first  heighest is : {numbers[-2]}")