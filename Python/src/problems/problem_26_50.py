'''
Created on Jun 7, 2012

@author: Administrator
'''
from lib import *
import itertools
import fractions
import collections
def problem_27():
    i_max=[0,0,0]
    for i in range(-1000,1000):
        for j in range(-1000,1000):
            for n in itertools.count(0):
                if not ext.XInt(n**2+i*n+j).isPrime():break
            if n>i_max[0]:i_max=[n,i,j]
    return i_max[1]*i_max[2]                

def problem_29():
    return len(set(i**j for i in range(2,101) for j in range(2,101)))

def problem_30():
    #return sum(i for i in range(2,4000000) if sum(int(j)**5 for j in str(i))==i)
    return sum(filter(lambda i: i == sum([int(x)**5 for x in str(i)]), range(2,400000)))

def problem_31():
    target = 200
    coins = [1,2,5,10,20,50,100,200]
    ways = [1]+[0]*target
    for coin in coins:
        for i in range(coin, target+1):
            ways[i] += ways[i-coin]
    return ways[target]

def problem_32():
    i_num='123456789'    
    a=set()
    for k in range(1,3):
        for i in itertools.permutations(i_num,k):
            i_temp=int(''.join(i))                      
            temp=''.join([s for s in i_num if s not in str(i_temp)])            
            if k==1:m=4
            else:m=3
            for j in itertools.permutations(temp,m):
                j_temp=int(''.join(j))                              
                if utilities.is_pandigital(str(i_temp)+str(j_temp)+str(i_temp*j_temp)):a.add(i_temp*j_temp) 
    return sum(a)
    
def problem_33():
    result=1
    for i in range(1,10):
        for j in range(i+1,10):
            for k in range(1,10):
                if fractions.Fraction(i*10+j,j*10+k)==fractions.Fraction(i,k):
                    result*=fractions.Fraction(i,k)
    return result.denominator
                                  
def problem_34():
    i_fact=[1,1,2,6,24,120,720,5040,40320,362880]
    #return sum(filter(lambda x:x==sum(i_fact[int(i)] for i in str(x)),range(3,400000)))    
    return sum(i for i in range(3,400000) if sum(i_fact[int(j)] for j in str(i))==i)

def problem_35():    
    num=0
    for i in range(100,1000000):
        if any(j in str(i) for j in ['0','2','4','6','8']):continue
        k,temp=0,i        
        while k<len(str(i)):
            temp=int(str(temp)[1::1]+str(temp)[0])
            if not ext.XInt(temp).isPrime():break
            k+=1
        else:num+=1            
    return num+13
    """
    n=0
    for i in range(100,1000000):
        for j in itertools.permutations(str(i),len(str(i))):
            if len(j)!=len(str(i)) or not ext.XInt(int(''.join(j))):break
        else:
            n+=1
            print(locals())
    return n+13
    #return len(list(j for i in range(100,1000000) for j in itertools.permutations(str(i),len(str(i)))  if len(j)==len(str(i)) and ext.XInt(int(''.join(j)))))+13  
    """
              
def problem_36():    
    return sum(i for i in range(1,1000000) if ext.XInt(i).isPalindromic() and ext.XInt(bin(i)).isPalindromic()[:1:-1])
 
def problem_37():
    """
    http://en.wikipedia.org/wiki/Truncatable_prime
    http://en.wikipedia.org/wiki/List_of_prime_numbers
    2, 3, 5, 7, 23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397
    """   
    i_sum=set()
    n=0
    for i in itertools.count(11,2):    
        temp=str(i)            
        if '1' in temp[0]+temp[-1] or '9' in temp[0]+temp[-1] or '0' in temp or '4' in temp or '6' in temp or '8' in temp:continue
        for k in range(1,len(temp)):
            if not(ext.XInt(int(temp[:k+1])) and ext.XInt(int(temp[k:]))):break
        else:
            i_sum.add(temp)
            n+=1
        if n==11:break
    return sum(int(i) for i in i_sum)  
    
                   
def problem_38():    
    s_temp=['1', '2', '3', '4', '5', '6', '7', '8', '9']
    i_generator=iter(''.join(i) for i in itertools.permutations('123456789',8) if int(''.join(i))>18273645)
    s_ans=918273645
    for i in range(9234,9876):
        i_temp=str(i)+str(i*2)
        if sorted(i_temp)==s_temp and s_ans<int(i_temp):s_ans=int(i_temp)                                   
    for i in range(912,987):
        i_temp=str(i)+str(i*2)
        if sorted(i_temp)==s_temp and s_ans<int(i_temp):s_ans=int(i_temp)
    for i in range(91,98):
        i_temp=str(i)+str(i*2)
        if sorted(i_temp)==s_temp and s_ans<int(i_temp):s_ans=int(i_temp)
    for i in range(9,11):
        i_temp=str(i)+str(i*2)
        if sorted(i_temp)==s_temp and s_ans<int(i_temp):s_ans=int(i_temp)
    return s_ans

def problem_39():
    
    i_iter=iter((x,y,z) for x in range(4,500) for y in range(x,500) for z in range(y,500) if (x**2+y**2)==z**2 and x+y+z<1000)
    i_dict={}
    for i in i_iter:
        if sum(i) not in i_dict:
            i_dict.update({sum(i):[i]})
        else:i_dict[sum(i)].append([i])
    return sum(max((value for value in i_dict.values()),key=len)[0])
    """       
    i_result=[0,0]
    for i in range(4,1000):
        j,i_num=1,0
        while j<i//2:
            k=1
            while k<(i-j)//2:
                if j**2+k**2==(i-j-k)**2:
                    i_num+=1
                k+=1
            j+=1
        #print("the I process is:",i)
        if i_num>i_result[1]:
            i_result[0]=i
            i_result[1]=i_num
    return i_result
    """
    
def problem_40():
    i_str=''
    for i in itertools.count(1):
        i_str+=str(i)
        if len(i_str)>=1000000:
            return int(i_str[0])*int(i_str[10-1])*int(i_str[100-1])*int(i_str[1000-1])*int(i_str[10000-1])*int(i_str[100000-1])*int(i_str[1000000-1])
        
        
def problem_41():
    s_num="123456789"
    return max(''.join(i) for j in range(2,10) for i in itertools.permutations(s_num[0:j],j) if ext.XInt(int(''.join(i))))
    """
    i=4
    i_result=0
    while i!=10:
        for k in itertools.permutations(s_num[0:i],i):
            a=''
            temp=int(a.join(k))
            if ext.XInt(temp) and temp>i_result:i_result=temp
        i+=1
    return i_result
    """           
def problem_42():    
    f_word=list(i.strip('"') for i in next(data.openfile('words.txt')).strip().split(','))
    #print(locals())
    d_dict=dict(zip((i for i in f_word),((sum(ord(j) for j in i)-len(i)*64) for i in f_word)))    
    b_set=set(n*(n+1)//2 for n in range(1,int((int(max(d_dict.values())*2)**0.5))))
    return sum(1 for i in d_dict.values() if i in b_set)
    """     
    f_len=max(len(i) for i in f_word)    
    i_result=0
    d_dict=dict(zip((chr(i) for i in range(65,91)),(i for i in range(1,27)))) 
    b_set=set(n*(n+1)//2 for n in range(1,int((f_len*27*2)**0.5)))
       
    for j in f_word:
        if sum(d_dict[k] for k in j) in b_set:i_result+=1
        #print(sum(ord(k) for k in j))
    return i_result
    """
    
def problem_43():
    s_num='0123456789'
    i_sum=0
    l_list=[2,3,5,7,11,13,17]
    for i in itertools.permutations(s_num,10):
        k=''
        s_str=k.join(i).lstrip('0')
        if len(s_str)==9:continue
        m=0
        while m!=7:
            if int(s_str[m+1:m+4])%l_list[m]!=0:
                break
            m+=1
        else:i_sum+=int(s_str)
        """
        if int(s_str[1:4])%2!=0:continue        
        elif int(s_str[2:5])%3!=0:continue
        elif int(s_str[3:6])%5!=0:continue
        elif int(s_str[4:7])%7!=0:continue
        elif int(s_str[5:8])%11!=0:continue
        elif int(s_str[6:9])%13!=0:continue
        elif int(s_str[7:10])%17!=0:continue
        else:i_sum+=int(s_str)
        """
    return i_sum       
        
def problem_44():
    p2=0  #just a bug
    pairs=((p1,p2)  for (n1,p1) in ((n,utilities.pentagonal(n)) for n in itertools.count(0))
           for p2 in (utilities.pentagonal(n) for n in range(1,n1))
           if euler_ceil.is_pentagonal(p1-p2) and euler_ceil.is_pentagonal(p1+p2))
    p1,p2=next(pairs)
    return p1-p2

def problem_45():
    return (a for a in (utilities.hexagonal(n) for n in itertools.count(143+1)) if euler_ceil.is_pentagonal(a)).__next__()
    """
    i_iter=(a for (n,a) in ((n,utilities.triangle(n)) for n in itertools.count(285+1)) for (i,b) in ((i,utilities.pentagonal(i)) for i in range(165,n)) for c in (utilities.hexagonal(j) for j in range(143,i)) if a==b==c)
    #i_iter.__next__()
    return i_iter.__next__()
    """
    
def problem_46()->"backlog=1":
    n = 5
    f = 1
    primes = set()
    while (1):
        if all( n % p for p in primes ):
            primes.add(n)           
        else:
            if not any( (n-2*i*i) in primes for i in range(1, n) ):break
        n += 3-f
        f = -f
    return n

def problem_47():
    i=642
    while True:             
        if len(ext.XInt(i).factors())-1!=4:
            i+=1
            continue
        elif len(ext.XInt(i).factors())-1!=4:
            i+=2
            continue
        elif len(ext.XInt(i).factors())-1!=4:
            i+=3
            continue
        elif len(ext.XInt(i).factors())-1!=4:
            i+=4
            continue
        else:return i
                           
def problem_48():
    i_result=0
    for i in range(1,1001):
        i_result=int(str(i_result+int(str(i**i)[:-11:-1][::-1]))[:-11:-1][::-1])
    return i_result

def problem_49():
    a=[i for i in ext.XInt(10000).sievePrime() if i>1000]
    for i in a:
        if i+3330 in a and i+6660 in a and sorted(str(i))==sorted(str(i+3330))==sorted(str(i+6660)) and i!=1487:
            return (str(i)+str(i+3330)+str(i+6660))
     
def problem_50():
    i_list=ext.XInt(1000000).sievePrime()
    a=itertools.accumulate(i_list)
    a=[i for i in a if i<1000000]
    for k in a[-1:]:
        j=0
        while k>953:
            if ext.XInt(k).isPrime():
                return k
            k=k-i_list[j]
            j+=1
    
        