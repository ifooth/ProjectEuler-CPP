'''
Created on Jun 5, 2012

@author: Administrator
'''
import collections
import fractions

def isPrime(i_num):
    """ is a prime
    
    >>> isPrime(3197)
    False
    >>> isPrime(1)
    False
    """
    assert i_num>1,"I must be a positive integer"
    if i_num<2:return False
    elif i_num==2:return True
    elif not i_num&1:return False
    elif any((i_num%i)==0 for i in range(3,int(i_num**0.5)+1,2)):return False   
    return True

def factors_temp(i_num):
    yield 1
    i,limit=2,i_num**0.5
    while i<=limit:
        if i_num%i==0:
            yield i
            i_num//=i
            limit=i_num**0.5
        else:i+=1
    if i_num>1:yield i_num  
def factors(i_num):
    """Return a dict of of factors of a number
    
    >>> factors(28)
    {1: 1, 2: 2, 7: 1}
    >>> factors(1)
    {1: 1}
    """  
    cnt=collections.Counter()
    for j in list(factors_temp(i_num)):
        cnt[j]+=1    
    return dict(cnt)

        
def divisors(i_num):
    """
    
   
    
    """
    l_temp=factors(i_num)
    del l_temp[0]
    l_a=[]
    i_len=len(l_temp)
    i=0
    while i<i_len:
        j=1
        l_a.append([1])
        while j<=l_temp[i][1]:
            l_a[i].append(l_temp[i][0]**j)
            j+=1
        i+=1
    #print(l_a)   
    j=1
    l_result=l_a[0]
    while j<len(l_a):
        l_te=[]
        for t_m in l_a[j]:
            for t_n in l_result:
                l_te.append(t_m*t_n)
        l_result=l_te
        j+=1
    #print(l_result)
    return l_result

def sumOfDivisors(i_num):
    """
    counts the number of positive integers less than or equal to n that are relatively prime to n
    
    """
    assert i_num>0,"I must be a positive integer and must be exceed 1"
    if i_num==1:return 0
    i_sum=1
    for key,value in factors(i_num).items():        
        i_sum*=sum(key**i for i in range(value+1))
    return i_sum//2-i_num

def numberOfDivisors(i_num):
    """
    number of divisors
    """
    assert i_num>0
    if i_num==1:return 1
    else:
        i_sum=1
        for value in factors(i_num).values():
            i_sum*=(value+1)
        return i_sum//2

def phi(i_num):
    """
    counts the number of positive integers less than or equal to n that are relatively prime to n
    
    >>> phi(9)
    6
    """
    i_result=1
    d_temp=factors(i_num)
    d_temp.pop(1)
    for key,value in d_temp.items():
        i_result*=(key**value-key**(value-1))
    return i_result

def recurringDecimalToFraction(i_str):
    """
    1
    1.01
    1.2(3244)
    """
    if '(' not in i_str:return fractions.Fraction(i_str)
    else:
        i_num=[i.split('(') for i in i_str.strip(')').split('.')]        
        i_den='9'*len(i_num[1][1])+'0'*len(i_num[1][0])        
        i_n=int(i_num[0][0])*int(i_den)+int(i_num[1][0]+i_num[1][1])-int(i_num[1][0])        
        return fractions.Fraction(int(i_n),int(i_den))
    if type(i_str)==type(fractions.Fraction()):
        i_num=i_str.numerator
        i_den=i_str.denominator
        temp=divmod(i_num,i_den)
        l_temp=[temp[1]*10]
        l_result=[temp[0],'.']
        while i not in l_temp:
            pass
            
        
def continueFraction(l_list):
    l_result=[[l_list[0]]]
    l_t=l_list
    l_t.reverse()
    l_result=[1,l_t[0]]
    del l_t[0]
    #print(l_result)   
    
    for i in l_t:
        l_result[0]=i*l_result[1]+l_result[0]
        l_result.reverse()
        #print(l_result)
    l_result.reverse()    


     
def isPalindromic(i_num):       #i_num must a string
    return i_num == i_num[::-1]

def HCF(a,b):
    """ Highest Common Factor
    return a if b == 0 else gcd(b, a % b)
    """
    while b:a,b=b,a%b
    return a                         

def test():    
    import doctest
    doctest.testmod()
if __name__=="__main__":
    test()
    #print(factors(4648767868))
        
