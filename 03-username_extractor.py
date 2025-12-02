#!/usr/bin/env python
# Author: Aravind Basava
# Email : aravind@gmail.com
# user input : vishwas@cloudthat.com
# user name : vishwas

# user_inp = "vishwas@cloudthat.com"
# print(f"The extracted username is: {user_inp[:7]}")
 
user_inp = input("Enter the user email: ")
print(f"The extracted user name is : {user_inp[:user_inp.find('@')]}")