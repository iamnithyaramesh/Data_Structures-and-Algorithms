# -*- coding: utf-8 -*-
"""
This module provides ADTs Stack and Queue to facilitate stack-based
and queue-based array implementations. This is  a part of the code of problem 1 of part A 
of the exercise 9 given under the course (Programming and Data Structures).

This is a sample implementation and may contain bugs!
We have tried to follow good coding practices but don't
claim that this source code is perfect!

Your comments and suggestions are welcome.

Created on Wed Apr 05 2023

Revised on Sat Apr 08 2023

Original Author:R.Nithyasri(IT-B)[Reg No:3122 22 5002 086]
"""

# Class Definitions

#1. This is the class Queue

class Queue:

    ''' ADT for the execution of Queue-based Implementations

    Data Member: self.queue-[]

    Member Functions:    __init__
                         isempty
                         isfull
                        enqueue
                        dequeue
                         __str__
                         __len__
                '''


    
    #Member Function : __init__
    def __init__(self):

        ''' This is the constructor function of the class. Initializes
        an empty queue to the object of the class'''
        self.queue=[]

    #Member Function: __isempty__    
    def isempty(self):

        '''Checks if the queue is empty - length comparison'''

        if len(self.queue)==0:
            return True

    #Member Function: __isfull__    
    def isfull(self):

        ''' Check if the queue is full - Invalidity of the isempty() condition'''

        if self.__isempty__()==False:
            return True

    # Member Function: enqueue
    def enqueue(self,element):

        ''' Performs the enqueue operation on the  class object  - append operation at the rear end'''

        self.queue.append(element)

    # Member Function : dequeue
    def dequeue(self):

        ''' Performs the dequeue operation on the class object and returns the value
          - pop the first element '''

        x=self.queue.pop(0)
        return x
    
    # Member Function : __len__
    def __len__(self):

        ''' Returns the length of the Queue object'''

        return len(self.queue)
    
    # Member Function : __str__
    def __str__(self):

        ''' Prints the class object'''
        return str(self.queue)

# End of the class Queue

# This is the class Stack
class Stack:

    ''' ADT for the execution of Stack-based Implementations

    Data Member: self.stack-[]

    Member Functions:    __init__
                         isempty
                         isfull
                        push
                        pop
                        top_element
                         __str__
                         __len__
                         __setitem__
                         __getitem__
                '''
    
    # Member Function : __init__
    def __init__(self):

        ''' This is the constructor function of the class. Initializes
        an empty stack to the object of the class'''

        self.stack=[]

    #Member Function : isempty    
    def isempty(self):

        '''Checks if the stack is empty - length comparison'''

        if len(self.stack)==0:
            return True
        else:
            return False

    #Member Function : isfull    
    def isfull(self):

        ''' Check if the stack is full - Invalidity of the isempty() condition'''

        if not self.isempty():
            return True

    # Member Function : push    
    def push(self,element):

        ''' Performs the push operation on the  class object  - append operation'''

        self.stack.append(element)

    # Member Function : pop
    def pop(self):

        ''' Performs the pop operation on the class object and returns the value
          - pop the last element '''
        
        x=self.stack.pop()
        return x
    
    # Member Function : top_element
    def top_element(self):

        ''' Returns the top element of the stack object - the last element'''

        return self.stack[len(self.stack)-1]
    
    # Member Function : __len__
    def __len__(self):

        ''' Returns the length of the Stack object'''

        return len(self.stack)
    
    # Member Function : __str__
    def __str__(self):

        ''' Prints the class object'''

        return str(self.stack)
    
    #Member Function : __getitem__
    def __getitem__(self,index):

        ''' Fetches the item at a particular index from within the stack'''

        return self.stack[index]
    
    # Member Function : __setitem__
    def __setitem__(self,index,value):

        ''' Assigns a value to the particular index of the class object'''

        self.stack[index]=value
    






    

        
    
        

    




        
