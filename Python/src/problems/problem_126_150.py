'''
Created on 2012-7-18

@author: botwave
'''
from lib import *
def problem_134():
    s=[i for i in ext.XInt(1000000).sievePrime() if i>3]
    #s.append(1000003)
    #s=[999983,1000003]
    #s=[19,23]
    #s=[221,223]    
    s_sum=0   
    for i in range(len(s)-1):
        result=[]
        for j in [1,3,5,7,9]:            
            if str(s[i+1]*j)[-1] is str(s[i])[-1]:
                result.append(j)                
                temp=s[i+1]*j                
                for n in range(2,len(str(s[i]))+1):
                    for m in [1,2,3,4,5,6,7,8,9]:                    
                        if str(m*s[i+1]+int(str(temp)[-n]))[-1] is str(s[i])[-n]:
                            result.append(m)
                            temp=temp+m*s[i+1]*(10**(n-1))                            
                            break
        result.reverse()                       
        t=''
        for f in result:
            t+=str(f)        
        s_sum+=s[i+1]*int(t)
    print(s_sum)            
        
        
            
                            
                    
problem_134()           