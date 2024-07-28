# -*- coding: utf-8 -*-
"""
This module provides a method of two - way stack implementation on a single
array. This is the implementation part of the code of 
problem 1 of part A of the exercise 9 given under the course 
(Programming and Data Structures).

This is a sample implementation and may contain bugs!
We have tried to follow good coding practices but don't
claim that this source code is perfect!

Your comments and suggestions are welcome.

Created on Mon Jun 05 2023

Revised on Wed Jun 07 2023

Original Author:R.Nithyasri(IT-B)[Reg No:3122 22 5002 086]
"""

import ctypes

# This is the class StackOps

class StackOps:

    ''' The class performs the two-way stack implementation
    with elements entering at both the start and end of the list
    
    '''

    # This is the constructor of the class
    def __init__(self,cap):

        '''Assigns the data members and initializes an empty array namely self.A'''

        self.cap=cap
        self.A=self.makearray(cap)
        self.top1=0                     # Initializing the entry pointers
        self.top2=cap-1
    
    # Member Function : makearray
    def makearray(self,cap):

        ''' The function makes use of the py_object method under
         the ctypes module to create an array of the required capacity '''
        
        temp=(cap*(ctypes.py_object))()
        return temp
    
    #Member Function : push
    def push(self,index,element):

        ''' The function pushes an element at the mentioned position
        (start or end entry point) in the array  -- check condition
        (StackFull Condition) '''

        if StackOps.isfull(self)==False:
         if index==0:                       #Insertion at the start of the array
            self.A[self.top1]=str(element)
            self.top1+=1
         elif index==1:                     #Insertion at the end of the array
            self.A[self.top2]=str(element)
            self.top2-=1
        else:                               #Exception Raise
            raise Exception

    # Member Function : isempty()        
    def isempty(self):

        ''' Checks if the array is empty ---> when both the pointers
        are in the initial condition as defined by the constructor'''

        if self.top1==0 and self.top2==self.cap:
            return True
        else:
            return False

    #Member Function : isfull()    
    def isfull(self):

        ''' Checks if the array is full --->  pointer position check'''

        if self.top1>self.top2:
            return True
        else:
            return False
    
    # Member Function : __str__
    def __str__(self):

        ''' Prints the class object'''

        return "<"+str(self.A)+">"


# Driver Code

''' Appropriate testcases are to be given to check the validit of the code'''

s=StackOps(10)

s.isempty()
s.push(0,1)
s.push(0,2)
s.push(0,3)
s.push(0,4)
s.push(0,5)

s.push(1,1)
s.push(1,2)
s.push(1,3)
s.push(1,4)
s.push(1,5)

# Since the mentioned capacity is 10, any push operation made further will result in an exception raise.




    
    

    
    
