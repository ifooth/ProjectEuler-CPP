'''
Created on Jun 9, 2012

@author: Administrator
'''
from lib_euler import *
def problem_108():    
    for i in range(30030,510510):
        if ((euler_math.lib_numberOfDivisors(i**2)+1)//2)>1000:
            print((euler_math.lib_numberOfDivisors(i**2)+1)//2)
            break
        #print((euler_math.lib_numberOfDivisors(i**2)+1)//2)
        #print("the i process is:",i)    
    return i