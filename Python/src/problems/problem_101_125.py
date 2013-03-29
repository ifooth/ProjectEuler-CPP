'''
Created on Jun 9, 2012

@author: Administrator
'''
from lib import *
def problem_111():
    a=[i for i in ext.XInt(10000).sievePrime() if i>1000]
    import collections    
    return a
def problem_108():    
    return data.openfile("names.txt").__next__()
def problem_103():
    pass
def problem_113():
    n=100
    return util.binomial(n+10,10)+util.binomial(n+9,9)-10*n-2
def problem_116():
    color=[2,3,4]
    limit=50
    num=0
    i=0
    while i<3:
        k=1
        while k*color[i]<limit:
            num+=((limit-color[i]*k)*k+1)
            k+=1
        i+=1
    return num
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
