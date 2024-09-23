#!/usr/bin/env python
# coding: utf-8

# # Unit 4 Career Preparation: Technical Assessment
# ## Problem 1

# Write a script that:
# * Reads the file `problem1.txt`.
# * Adds each line to a new list.
# * Prints the new list.

# In[55]:


#Goals: read the file, add each line to a list, print the list
#Input: file of strings 
#Output: list of strings

#Import the operating system
import os
#Define the file and list
file = "problem1.txt"
list = []
#open the file
open_file = open(file, "r")
#iterate the list
for line in open_file:
    #append list with lines
    list.append(line)
#print the list
print(list)
#close the file
open_file.close()
        


# ## Problem 2
# 
# Write a script that:
# *  Reads the file `problem2.txt`.
# *  Counts how many times 192.168.1.1 appears in the file.
# *  Prints the result.

# In[56]:


#Goals: read the file, count how many times 192.168.1.1 appears, print results
#Input: Ip addresses : strings 
#Output: a count of how many times 192.168.1.1 appears

#import the OS
import os
#define the file and counter
file = "problem2.txt"
count = 0
#open the file
open_file = open(file, "r")
#iterate over the lines
for line in open_file:
    #find the ip address we are looking for and strip any extra spaces
    if line.strip() == "192.168.1.1":
        #count how many times it appears
        count += 1
#print the results
print(count)


# ## Problem 3
# Write a script using a function (`dedupe`) that:
# * Takes a list `l = [1,5,7,2,4,3,5,1,6,2,6]`.
# * Returns a new list that contains all of the elements from the first list, excluding duplicates.

# In[57]:


#Goals: create a function (dedupe), remove duplicates from list
#Input: List of integers
#Output: new list of original numbers(no duplicates)

#define the function and lists
def dedupe(list):
    originals = []
    duplicates = []
    #iterate the list
    for number in list:
        #put numers in correct list
        if number in originals and number not in duplicates:
            duplicates.append(number)
        else:
            originals.append(number)
    #return original numbers
    return originals
#define our input list
l = [1,5,7,2,4,3,5,1,6,2,6]
#run our function with input list as arguemnt
originals = dedupe(l)
#print results
print(originals)
    
    


# ## Problem 4
# 
# Write a program (using a function) that:
# * Asks the user for a long string containing multiple words.
# * Prints back the same string, except with the words in reverse order.
# 
# For example, if the user types the string: 'My name is robert', it will print 'robert is name My'.

# In[59]:


#Goals: take user input,print the same input in reverse
#Input: string : user input
#Output: string : print the exact string, but reversed

#receive our string from user and convert to list using split function
original_list = input("Please enter multiple words").split()
#reverse the list of strings
reversed_list = original_list[::-1]
#print the reversed string
print(reversed_list)


# ## Problem 5
# 
# Write a script that:
# * Opens the file `problem5.txt`.
# * Counts each port and puts the results in a dictionary.

# In[ ]:


#Goals: open the file, count each port, create a dictionary
#Input: integers, ports
#Output: dictionary: with counts of each port

#define the dictionary and file
port_count = {}
file = "problem5.txt"
#open the file
open_file = open(file, "r")
#iterate over the file
for line in open_file:
    #strip excess spaces or uneccesary lines to get only port numbers
    port = line.strip()
    #check if port has already been seen
    if port in port_count:
        #adds 1 occurance to count
        port_count[port] += 1
    else:
        #else, creates dictionary index for port
        port_count[port] = 1
#print results
print(port_count)
    


# In[ ]:




