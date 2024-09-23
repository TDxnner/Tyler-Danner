#!/usr/bin/env python
# coding: utf-8

# # Unit 4: Challenge
# 
# ## Problem 1 
# 
# 1. Open the `exam.log` file.
# 
# 
# 2. Write a function ```ip_result``` that:
# * Searches for lines with IP
# * Counts the number of each IP
# * Puts the results in a dictionary
# * Sorts the dictionary 
# * Puts the results into a file
# 
# 3. Write a function ```invalid_user_count``` that:
# 
# * Searches for invalid user logins 
# * Counts the invalid  logins for each user 
# * Puts the results in a dictionary
# * Sorts the dictionary
# * Puts the result into a file 
# 
# 4. Write a function `failed_logins` that:
# 
# * Searches for wrong passwords
# * Counts the failed logins
# * Puts the results in a dictionary
# * Sorts the dictionary
# * Puts the result in a file
# 
# 5. Call the functions

# In[ ]:


#import the os and regex
import os
import re

#define function #1
def ip_results(file):
    #define the ip dictionary
    ip_address = {}
    #iterate each line in the file
    for line in open_file:
        #see if the line contains an IP address
        if line == /(?:\d{1,3}\.){3}\d{1,3}/:
            #if it does, add it to the dictonary
            ip_address[line] += 1
    #sort the dictionary
    sorted_ip = ip_address.sorted()
    return 

#define function #2
def invalid_user_count(file)
    #define the invalid user dictionary
    invalid_user = {}
    #iterate each line in the file
    for line in open_file:
        #see if the line contains an invalid user
        if line == "invalid user":
            #if it does, add it to the dictonary
            invalid_user[line] += 1
    #sort the dictionary
    sorted_invalid_user = invalid_user.sorted()
    return

#define function #3
def failed_logins(file)
    #define the failed logins dictionary
    failed_login = {}
    #iterate each line in the file
    for line in open_file:
        #see if the line contains a failed login attempt
        if line == "failed login":
            #if it does, add it to the dictonary
            failed_login[line] += 1
    #sort the dictionary
    sorted_failed_login = failed_login.sorted()
    return

#define the file
file = "exam.log"
#open file
open_file = open(file, "r") 
#call the functions
ip_results(open_file)
invalid_user_count(open_file)
failed_logins(open_file)


# ## Problem 2 
# Analyze the following code that reads the `apache_logs.txt` file. Determine what it does. Write your response as code comments.

# In[ ]:


import sys
import os

#define function (readfile) with f as an argument
def readfile(f):
    #open a file
    openfile = open(f,"r")

    #opening 3 files, 'uniqueIP.txt, allIP.txt, ipAndUrl.txt
    unique_outfile = open("uniqueIP.txt","w")
    all_outfile = open("allIP.txt","w")
    ipAndUrl_outfile = open("ipAndUrl.txt","w")

    #define the lists and dictionaries
    lines = []
    ipAndUrl = {}
    ip_list = set()

    #puts each line in a list
    for line in openfile:
        lines.append(line.strip('\n'))

    #take the list from before, splits using space, sets the ip variable using the index of the IP
    for line in lines:
        ip = line.split(" ")[0]
        #If the IP is in the file: ipAndURL.txt, it will append the URL which is in the 6th index
        if ip in ipAndUrl:
            ipAndUrl[ip].append(line.split(" ")[6])
        #else, it will create a new variable for that specific IP
        else:
            ipAndUrl[ip] = [line.split(" ")[6]]
        #add the ip to the all_outfile and starts a new line for the next IP
        all_outfile.write(ip)
        all_outfile.write("\n")
        # adds the IP to the ip_list
        ip_list.add(ip)
    # add the ip to the unique_outfile and starts a new line for the next IP
    for ip in ip_list:
        unique_outfile.write(ip)
        unique_outfile.write("\n")
    #???
    for key, value in ipAndUrl.items(): 
        ipAndUrl_outfile.write('%s  %s\n' % (key, value))
# closes all files being used when done
    unique_outfile.close()
    ipAndUrl_outfile.close()
    all_outfile.close()
    openfile.close()
#defining the main function
def Main():
    #take a user input containing a file name
    file=input("please enter a file name: ")
    #reads the file input and sets it as a varible named results
    result = readfile(file)

#determine if the script is being run directly or imported as a module   
if __name__ == '__main__':
      
    Main()


# In[ ]:




