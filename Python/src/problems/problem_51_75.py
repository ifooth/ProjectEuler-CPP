'''
Created on Jun 7, 2012

@author: Joe Lei
'''

import logging
log=logging.getLogger(__name__)

from lib.ext import intx,fractionx
import math
import itertools
import string

def eight_prime_family(prime,rd):
    c=0
    for digit in '0123456789':
        n=int(prime.replace(rd,digit))
        if (n>100000 and intx(n).isPrime()):
            c=c+1
    return c==8
def problem_51():
    for prime in intx(1000000).sievePrime():
        if prime>100000:
            s=str(prime)
            last_digit=s[5:6]
            if (s.count('0')==3 and eight_prime_family(s,'0') or \
                s.count('1')==3 and last_digit!='1' and eight_prime_family(s,'1') or \
                s.count('2')==3 and eight_prime_family(s,'2')):return s            
    k=3
    result=[]
    for i in range(1,10):
        if intx(i*10+k).isPrime():result.append(i*10+k)          
    return result
    
def problem_52():
    return (i for i in itertools.count(6) if sorted(str(i))==sorted(str(i*2))==sorted(str(i*3))==sorted(str(i*4))==sorted(str(i*5))==sorted(str(i*6))).__next__()
    
def problem_53():
    return len(list((i,j) for i in range(1,101) for j in range(1,i+1) if math.factorial(i)/(math.factorial(j)*math.factorial(i-j))>1000000))

def problem_54(): #Diamond Club Heart Spade
    pass
               
    
def problem_55():
    i_result=0
    for i in range(1,10000):
        n=0
        while n<50:
            i=i+int((str(i)[::-1]))
            if ext.EInt(i).isPalindromic():
                break
            n+=1
        else:
            i_result+=1
    return i_result

def problem_56():
    #return sum(int(i) for i in (str(a**b) for a in range(1,100) for b in range(1,100)))
    i_result=0
    for i in range(1,100):
        for j in range(1,100):
            i_result=max(i_result,sum(int(k) for k in str(i**j)))
    return i_result    
            
def problem_57():
    l_t=[1]+[2]*99
    l_t.reversed()
    l_result=[1,l_t[0]]
    del l_t[0]
    for i in l_t:
        l_result[0]=i*l_result[1]+l_result[0]
        l_result.reverse()
def problem_59():
    i_str=list(next(data.openfile('cipher1.txt')).strip().split(','))    
    i_result=[]
    for i in itertools.combinations('abcdefghijklmnopqrstuvwxyz',3):
        for j in (itertools.islice(i_str,k,k+3) for k in range(0,len(i_str),3)):
            i_result.append(chr(m|n) for m in i for n in j)
    return i_result            
                                   

            
def problem_62():
    l_lis=[]
    for i in range(1,20000):
        l_lis.append(i**3)
    #l_lis=set(l_lis)
    l_result=[0,0,0,0,0]    
    for m in l_lis:
        n=0
        for j in l_lis:
            if sorted(str(m))==sorted(str(j)):
                l_result[n]=j
                n+=1
                if n==5:
                    print(l_result)
                    return m
def problem_65():
    l_t=[2]+[1]*99    
    if (len(l_t)-1)%3==2:
        l_t[2::3]=[i*2 for i in range(1,(len(l_t)-1)//3+2)]
    else:
        l_t[2::3]=[i*2 for i in range(1,(len(l_t)-1)//3+1)]
    #print(l_t)
    l_t.reverse()
    l_result=[1,l_t[0]]
    del l_t[0]
    #print(l_result)   
    
    for i in l_t:
        l_result[0]=i*l_result[1]+l_result[0]
        l_result.reverse()
        #print(l_result)
    l_result.reverse()    
    print(l_result)
    i_sum=0
    for i in str(l_result[0]):
        i_sum+=int(i)
    print(i_sum)
                   
def problem_70():
    t_result=100  
    for i in range(1,10000000):
        #i_result=min((t_result,(i/lib_math.phi(i) if sorted(str(i))==sorted(str(lib_math.phi(i)))))) 
        if sorted(str(i))==sorted(str(ext.EInt(i).phi())):
            t_result=min(t_result,i/ext.EInt(i).phi()) 
    return t_result

def problem_71():
    a=[1,1]
    limit=1000000
    i=limit-1
    j=limit//7*3          
    while a!=[j,i]:
        if a[0]/a[1]<3/7:                        
            a[0]+=1            
        else:
            a[1]+=1
    return a[0]-1

def problem_74():
    i_result=0
    fac_temp=[1,1,2,6,24,120,720,5040,40320,362880]
    for i in range(1,1000000):
        n=0
        i_sum=i
        s_set=set()
        s_set.add(i)
        while n<59:
            #temp=str(i_sum)
            i_sum=sum(fac_temp[int(j)] for j in str(i_sum))                       
            #for j in temp:
            #    i_sum+=fac_temp[int(j)]
            if i_sum in s_set:break
            else:s_set.add(i_sum)
            #s_set.add(i_sum)
            n+=1
        #if len(s_set)==60:
        #    i_result+=1
        else:i_result+=1
    return i_result            

        
    
    
    
    