#!/usr/bin/env python
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
 
from datetime import datetime
 
# Common Log file
LOG_FILE = "summary.log"
MAX_LINE_WIDTH = 80
# Define Functions to
# count the number of words
def num_words(inp_str):
    return len(inp_str.split())
# Count the number of Characters
def num_chars(inp_str):
    return len(inp_str)
# Count the number of lines
def num_lines(inp_str):
    return len(inp_str.split('\n'))
# Count the number of vowels
def num_vowels(inp_str):
    vowels = 'aeiou'
    return len(list(filter(lambda x: x in vowels, inp_str)))
# reading the file
def read_file(fname):
    try:
        with open(fname) as fh:
            return fh.read()
    except FileNotFoundError:
        print("File you are trying to read does not exist")
# writing to log
def write_log(LOG_FILE,**kwargs):
    with open(LOG_FILE, 'a+') as fh:
        fh.writelines(f"Summary of file {kwargs["file"]} on {datetime.now()}\n")
        fh.writelines("-"*MAX_LINE_WIDTH+"\n")
        for k,v in kwargs.items():
            fh.writelines(f"{k}:{v}\n")
 
# main function
def main():
    file_name = input("enter the fileame to summarize: ")
    content = read_file(file_name)
    summary_dict = {
        "file": file_name,
        "Number of Characters": num_chars(content),
        "Number of lines": num_lines(content),
        "Number of words": num_words(content),
        "Number of vowels": num_vowels(content)
    }
    # write_log(LOG_FILE,file=filename,number_of_chars=numchars(content),number_of_ords=num_words(content))
    write_log(LOG_FILE,**summary_dict)
 
if __name__ == '__main__':
    main()