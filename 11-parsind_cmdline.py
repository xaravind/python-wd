#!/usr/bin/env python

 
import argparse
 
parser = argparse.ArgumentParser(description="A script to calculate")
 
# parser.add_argument("number", help="This is a number")
parser.add_argument("-v", "--version", default="1", help="Displays the version")
 
args = parser.parse_args()
 
if args.version:
    print("version 1")
else:
    # print(f"The passed number is: {args.number}")
    print(f"This is an else block")
 