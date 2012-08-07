'''
Created on Jun 7, 2012

@author: Administrator
'''
from euler.lib import *
import decimal
def problem_79():
    mydata=[i.strip() for i in data.openfile('keylog.txt')]
    key=mydata[0]          
    print(mydata)
def problem_80():
    decimal.getcontext().prec=102    
    i_sum=0
    l_temp=set(i*i for i in range(1,10))
    for i in filter(lambda x:x not in l_temp,range(2,100)):
        if i in l_temp:continue
        i_sum+=sum(int(i) for i in str((decimal.Decimal(i).sqrt()*10**99))[0:100:1])
        #print(str((decimal.Decimal(i).sqrt()*10**99)))
    return i_sum
        
        
def problem_92():    
    s_set=set()
    for i in range(2,10000000):
        temp=i
        s_temp=set()
        while temp!=89:
            temp=sum(int(j)**2 for j in str(temp))
            if temp==1:break
            elif temp not in s_temp:s_temp.add(temp)
            else:break            
        else:
            s_set.update(s_temp)
    return len(s_set)
def problem_95():
    i_result=[0,0]    
    for i in range(220,1000):
        temp=ext.XInt(i).sumOfDivisors()
        n=1
        if temp==1:continue
        while i!=temp:            
            temp=ext.XInt(temp).sumOfDivisors
            n+=1
            if temp==1 or temp>1000:break
        else:
            if i_result[0]<n:i_result=[n,i]
    return i_result
problem_79()