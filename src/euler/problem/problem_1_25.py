'''
Created on Jun 7, 2012

@author: Administrator
'''


import itertools
import functools
import operator
import math
import datetime

from euler.lib import *

def problem_1():
    return sum(i for i in range(1000) if i%3==0 or i%5==0)

def problem_2():
    l_list=[1,2]
    while l_list[-1]<4000000:
        l_list.append(l_list[-1]+l_list[-2]) 
    #print(l_list[:-1])   
    return sum(i for i in l_list[:-1] if i%2==0)

def problem_3():   
    return max(lib_math.factors(600851475143))

def problem_4():
    return max(x*y for x,y in itertools.product(range(100,1000),range(100,1000)) if lib_math.isPalindromic(str(x*y)))

def problem_5():
    d_temp={1:1}
    for i in range(1,20):
        for key,value in lib_math.factors(i).items():
            if key not in d_temp or value>d_temp[key]:d_temp.update({key:value})
    #print(d_temp)    
    return functools.reduce(operator.mul,(key**value for key,value in d_temp.items()))

def problem_6():
    return abs(sum(i**2 for i in range(1,101))-sum(i for i in range(1,101))**2)

def problem_7():    
    n,i=1,3
    while n!=10001:
        if lib_math.isPrime(i):n+=1
        i+=2
    else:return i-2
    """
    s_prime={2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,79, 83, 89, 97}
    j=101
    while len(s_prime)!=10001:
        for k in s_prime:
            if j%k==0:break
        else:s_prime.add(j)
        j+=2
    return max(s_prime)
    """

def problem_8():
    i_str=''.join(lib_data.problem8.strip().splitlines())
    """   
    i_temp=[]
    for i in range(len(i_str)-4):        
        i_temp.append(functools.reduce(operator.mul,(int(j) for j in i_str[i:i+5])))
    return max(i_temp)
    """
    return max(functools.reduce(operator.mul,(int(j) for j in i_str[i:i+5])) for i in range(len(i_str)-4))
    
def problem_9():
    for i in range(1,1000):
        for j in range(i,1000):
            if i**2+j**2==(1000-i-j)**2:
                return i*j*(1000-i-j)
                  
def problem_10():
    return sum(i for i in range(3,2000000,2) if lib_math.isPrime(i))+2

def problem_11()->"Backlog==1":
    grid=[map(int,i.split()) for i in lib_data.problem11.strip().splitlines()]
    diffs=[(0, +1), (+1, 0), (+1, +1), (+1, -1)]
    sr,sc = len(grid),len(grid[0])
    return
    i_str=[i.split() for i in lib_data.problem11.strip().splitlines()]
    for i in range(20):
        for j in range(17):
            # maximum product from horizontal and vertical lines
            phv=max(int(i_str[i][j])*int(i_str[i][j+1])*int(i_str[i][j+2])*int(i_str[i][j+3]),int(i_str[j][i])*int(i_str[j+1][i])*int(i_str[j+2][i])*int(i_str[j+3][i]))
            if i<16:
                # maximum product from both diagonals
                pd=max(int(i_str[i][j])*int(i_str[i+1][j+1])*int(i_str[i+2][j+2])*int(i_str[i+3][i+3]),int(i_str[i][j+3])*int(i_str[i+1][j+2])*int(i_str[i+2][j+1])*int(i_str[i+3][j]))
    return max(phv,pd)

def problem_12():
    return (i for i in itertools.accumulate(itertools.count(1)) if lib_math.numberOfDivisors(i)>500).__next__()

def problem_13():        
    return str(sum(int(i) for i in lib_data.problem13.strip().splitlines()))[:10]

def problem_14():
    n=[0,0]
    for i in range(2,1000000):
        temp=i
        k=0
        while i!=1:
            if i&1:i=i*3+1
            else:i//=2
            k+=1
        else:
            if n[0]<k:n=[k,temp]
    return n[1]
        
def problem_15():
    return math.factorial(40)//(math.factorial(20)**2)

def problem_16():
    return sum(int(i) for i in str(2**1000))

def problem_17():
    d_word={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',\
            16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred',\
            1000:'thousand','a':'and'}
    i_sum=''    
    for i in range(1,100):
        if len(str(i))==1:
            i_sum+=d_word[i]
            #print(d_word[i])
        elif len(str(i))==2:
            if i<=20 or i%10==0:
                i_sum+=d_word[i]
                #print(d_word[i])
            else:
                i_sum+=(d_word[i//10*10]+d_word[i%10])
                #print(d_word[i//10*10]+d_word[i%10])
    i_temp=i_sum    
    for j in range(1,10):
        i_sum+=(d_word[j]*99+d_word[100]*99+d_word['a']*99+i_temp)
        i_sum+=(d_word[j]+d_word[100])
    i_sum+=d_word[1]+d_word[1000] #1000
    return len(i_sum)

def problem_18()->"Backlog==2":
    i_str=[map(int,i.split()) for i in lib_data.problem18.strip().splitlines()]            
    itertools.product([0,+1],repeat=len(i_str)-1)

def problem_19():
    return len(list((j,i,1)  for i in range(1,13) for j in range(1901,2001) if datetime.date(*(j,i,1)).weekday()==6))

def problem_20():
    return sum(int(i) for i in str(math.factorial(100)))

def problem_21():
    return sum(i for i in range(2,10000) if i!=lib_math.sumOfDivisors(i) and i==lib_math.sumOfDivisors(lib_math.sumOfDivisors(i)))

def problem_22():
    i_str=sorted([i.strip('"') for i in next(lib_data.openfile('names.txt')).strip().split(',')])
    #print(type(next(data.openfile('names.txt'))))              
    return sum((i+1)*sum(ord(j)-64 for j in i_str[i]) for i in range(len(i_str)))

def problem_23():    
    l_abundant=set(i for i in range(1,28123) if lib_math.sumOfDivisors(i)>i)
    return sum(i for i in range(28123) if not any((i-a in l_abundant) for a in l_abundant))
    """
    l_result=set(range(1,28123))
    for i in l_abundant:
        for j in l_abundant:
            if i+j in l_result:l_result.remove(i+j)
    return sum(l_result)          
    """
def problem_24():
    i_str='0123456789'
    #return len(list((itertools.permutations(i_str,10))))
    return ''.join(sorted(list(itertools.permutations(i_str,10)))[1000000-1])

def problem_25():
    i_sum=[1,1]    
    for i in itertools.count(3):
        i_sum=[i_sum[1],i_sum[1]+i_sum[0]]
        if len(str(i_sum[1]))==1000:return i
   
            
            
            
            