#!/usr/bin/env python
# Author: Aravind Basava
# Email : aravind@gmail.com
# script to find sum and average of n numbers taken from user
# until he enters -999 (exculing)

total = 0
count = 0
while True:
    num = int(input("Enter  the Number :"))
    if num ==  -999:
        break
    total += num
    count += 1


print("The sum of 10 numbers is : ", total)
# print("The avg of 10 numbers is : ", total/10)
# ways to print the ouput in same way with below formatters
# print("The average of 10 numbers is: "+str(total/10))
# print("The average of 10 numbers is: %f"%(total/10))
# print("The average of 10 numbers is: {0}".format(total/10))
print(f"The average of 10 numbers is: {total/10}")