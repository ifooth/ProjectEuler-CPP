'''
Created on Jun 9, 2012

@author: Administrator
'''
from euler.lib import *
def problem_108():    
    pass
def problem_117():
    color=[2,3,4]    
    limit=5    
    num=1
    i=0
    while i<3:
        k=1
        while k*color[i]<limit:
            num+=((limit-(color[i]*k))*k+1)
            k+=1
        i+=1
    a={2:limit//2,3:limit//3,4:limit//4}    
    return num