#!/usr/bin/env python
# Author: Aravind Basava
# Email : aravind@gmail.com
# script to find sum and average of 10 numbers taken from user

total = 0
for i in range(10):
    num = int(input("Enter  the Number :"))
    total += num

print("The sum of 10 numbers is : ", total)
# print("The avg of 10 numbers is : ", total/10)
# ways to print the ouput in same way with below formatters
# print("The average of 10 numbers is: "+str(total/10))
# print("The average of 10 numbers is: %f"%(total/10))
# print("The average of 10 numbers is: {0}".format(total/10))
print(f"The average of 10 numbers is: {total/10}")