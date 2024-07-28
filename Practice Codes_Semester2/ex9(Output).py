# -*- coding: utf-8 -*-
"""
This module provides ADTs Stack and Queue to facilitate stack-based
and queue-based array implementations. This is the output implementation
part of the code of problem 1 of part A of the exercise 9 
given under the course (Programming and Data Structures).

This is a sample implementation and may contain bugs!
We have tried to follow good coding practices but don't
claim that this source code is perfect!

Your comments and suggestions are welcome.

Created on Wed Apr 05 2023

Revised on Sat Apr 08 2023

Original Author:R.Nithyasri(IT-B)[Reg No:3122 22 5002 086]
"""

# Importing the required classes from the python file 'ex9.py'
from ex9 import Stack
from ex9 import Queue

s=Stack()   # Creating objects for the required classes
q=Queue()


#Driver Code

''' Appropriate testcases are to be given to test the validity of the code'''

n=int(input("Enter a Number"))

''' Pushing and Enqueuing of the indivudual digits into the stack and queue resp.'''

while n>0:
    r=n%10
    s.push(r)
    q.enqueue(r)
    n//=10

''' Check Condition : The popped and dequeued element must be the same'''

flag=True
while len(s)>0 and len(q)>0:
    x=s.pop()
    y=q.dequeue()
    if x!=y:
        flag=False
if flag:
    print("Palindrome")
else:
    print("Not a palindrome")

    



