'''
Created on Jun 9, 2012

@author: Administrator
'''
from euler.lib import *
def problem_108():    
    for i in range(30030,510510):
        if ((lib_math.numberOfDivisors(i**2)+1)//2)>1000:
            print((lib_math.numberOfDivisors(i**2)+1)//2)
            break
        #print((lib_math.numberOfDivisors(i**2)+1)//2)
        #print("the i process is:",i)    
    return i