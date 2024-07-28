import math
# -*- coding: utf-8 -*-
"""
This module provides a Python program to design and analyze algorithms and perform 
empirical analysis of algorithms as well(Solving a polynomial expression with a code 
of time complexity in the order of n^2,in the order of nlogn, in the order of n)
This is a part of Exercise 04 under UIT2201 (Programming and Data Structures).


This is a sample implementation and may contain bugs!
We have tried to follow good coding practices but don't
claim that this source code is perfect!

Your comments and suggestions are welcome.

Created on Tue Apr 11 2023

Revised on Sun 07 May 2023

Original Author:R.Nithyasri(IT-B)[Reg No:3122 22 5002 086]

"""

# Function definitions

# 1 This is the function 'random_sequence_generator

import random
def random_sequence_generator(n,start,end):

    ''' The function takes in the number of
    elements of the sequence n, start value of range
    of elements,start and the end value of range of
    elements,end as input and returns a randomly 
    generated sequence ,l as output'''


    l=[]
    for i in range(n+1):
        l.append(random.randint(start,end))
    return l

# End of function 'random_sequence_generator'


# 2 This is the function 'power(x,y)'

def power(x,y):

    ''' The function takes in arguments 'x',
    the base and 'y',the power and returns the
    value of x raised to the power of y
    
    The time complexity of the code is O(logn)'''

    global ct
    ct += 1
    if(y == 0):
        return 1
    temp = power(x, int(y / 2))
   
    if (y % 2 == 0):
        t= temp * temp
        return t
    else:
        t=x * temp * temp
        return t

# End of the function 'power(x,y)'    


# 3 Polynomial evaluation using the Brute Force Method

def brute_force(seq):

    ''' The function takes in a sequence of coefficients 
        of polynomial and evaluates the expression using
        Brute Force approach. The time complexity of the
        program code is O(n^2)
        
        Returns: The asymptotic notation value of time
        complexity'''
    
    count=0
    x=eval(input("Enter value for x"))
    count+=1
    sum=0
    for i in range(len(seq)):
        t=1
        for j in range(1,len(seq)+1-i):
            count+=1
            t*=x
            sum+=t
    return count

# End of function 'brute_force(seq)


# 4 This is the function 'recursive_method(seq)

def recursive_method(seq):

    ''' The function takes in a sequence of 
    coefficients of a polynomial input and returns
    the asymptotic value of the time complexity
    for a value of 'x'
    
    Functions used: power(x,y)

    The time complexity of the code is O(nlogn)'''

    global ct
    ct=0
    degree = len(seq) - 1
    ct=1
    count2=0
    x=eval(input("Enter the value of x"))
    for coeff in seq:
        ct += 1
        prod = power(x,degree)
        count2 += prod*coeff
        degree -= 1
    return ct

# End of the function 'recursive_method(seq)'

# 5 This is the function 'horners_method(seq)'

def horners_method(seq):

    ''' The function takes in an input of a sequence of
    coefficients of a polynomial input 'seq' and evaluates
    the polynomial using Horner's method.
    
    The time complexity of the algorithm is of the O(n)
    
    Returns: The aymptotic notation value of time complexity
    for a value of 'n'
    '''

    count=0
    sum=0
    count+=1
    x=eval(input("Enter value for x"))
    count+=1
    for i in range(len(seq)):
       count+=1
       sum=sum*x+seq[len(seq)-1-i]
    return count

# The end of the 'horners_method(seq)    


#Driver code

''' Appropriate testcases are to be given to test
the validity of the code'''    


n=int(input("Enter degree of the polynomial"))
start=int(input("Enter start value of the random range"))
end=int(input("Enter end value of the random range"))

x1=random_sequence_generator(n,start,end) # Generating a random list

count_bf=brute_force(x1)
count_rm=recursive_method(x1)
count_hm=horners_method(x1)
             
# Ratio analysis for Brute Force Method

print('f(n)',count_bf)
print(count_bf/n)
print(count_bf/n**2)            #PS: Testing to be done n-10,100,1000,10000   
print(count_bf/(n*math.log2(n)))

'''# Ratio analysis for Recursive Method

print('f(n)',count_rm)
print(count_rm/n)
print(count_rm/n**2)            #PS: Testing to be done n-10,100,1000,10000   
print(count_rm/n**3)
print(count_rm/(n*math.log2(n)))

# Ratio analysis for Horner's Method
print("f(n)",count_hm)
print(count_hm/n)
print(count_hm/n**2)            #PS: Testing to be done n-10,100,1000,10000   
print(count_hm/(n*math.log2(n)))   ''' 
       
       
