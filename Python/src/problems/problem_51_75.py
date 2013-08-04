#encoding=utf-8
'''
Created on Jun 7, 2012

@author: Joe Lei
'''

import logging
log=logging.getLogger(__name__)

from lib.ext import intx,fractionx
from lib import data
import math
import itertools
import string
from collections import Counter

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
    
def problem_52():
    return (i for i in itertools.count(6) if sorted(str(i))==sorted(str(i*2))==sorted(str(i*3))==sorted(str(i*4))==sorted(str(i*5))==sorted(str(i*6))).__next__()
    
def problem_53():
    return len(list((i,j) for i in range(1,101) for j in range(1,i+1) if math.factorial(i)/(math.factorial(j)*math.factorial(i-j))>1000000))

class poker():
    '''2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
        heart 红桃 spade 黑桃 club 梅花 diamond 方块
    '''
    def __init__(self,card):
        self.cards=card.split(' ') 
        self.card1,self.card2=self.cards[:5],self.cards[5:]        
        self.val={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}

    def win(self):
        return self.hand(self.card1)>self.hand(self.card2)

    def hand(self,card):
        if self.RoyalFlush(card):
            log.info('%s is Royal Flush'%card)
            return 108
        elif self.StraightFlush(card):
            log.info('%s is Straight Flush'%card)
            return 107
        elif self.FourKind(card):
            log.info('%s is Four Kind'%card)
            return 106
        elif self.FullHouse(card):
            log.info('%s is Full House'%card)
            return 105
        elif self.Flush(card):
            log.info('%s is Flush'%card)
            return 104
        elif self.Straight(card):
            log.info('%s is Straight'%card)           
            return 103
        elif self.ThreeKind(card):
            log.info('%s is Three Kind'%card)  
            return 102
        elif self.TwoPairs(card):
            log.info('%s is Two Pairs'%card)  
            return 101
        elif self.OnePair(card):
            log.info('%s is One Pair'%card)  
            return 100
        else:
            #log.info('%s is HighCard : %s'%(card,self.HighCard(card)))  
            return self.HighCard(card) 


    def RoyalFlush(self,card): #card repr [TC,JC,QC,KC,AC]        
        c=Counter([i[1] for i in card])
        return sorted(''.join([i[0] for i in card])) == 'TJQKA' and len(c)==1

    def StraightFlush(self,card):
        c=Counter([i[1] for i in card])        
        return ''.join([i[0] for i in card]) in '23456789TJQKA' and len(c)==1

    def FourKind(self,card):
        p=Counter([i[0] for i in card])        
        c = sorted(''.join(list(str(p[i]) for i in p)))
        return c == '14'

    def FullHouse(self,card): #3+3+3+2+2
        p=Counter([i[0] for i in card])        
        c = sorted(''.join(list(str(p[i]) for i in p)))
        return c == '23'

    def Flush(self,card):
        ''' 如果花色数量为1 为同花'''        
        c=Counter([i[1] for i in card])        
        return len(c)==1

    def Straight(self,card):        
        return ''.join([i[0] for i in card]) in '23456789TJQKA'

    def ThreeKind(self,card): #3+1+1
        p=Counter([i[0] for i in card])        
        c = sorted(''.join(list(str(p[i]) for i in p)))
        return c == '113'

    def TwoPairs(self,card): #2+2+2+2+1
        p=Counter([i[0] for i in card])        
        c = sorted(''.join(list(str(p[i]) for i in p)))
        return c=='122'

    def OnePair(self,card): #2+2+1+1+1
        p=Counter([i[0] for i in card])        
        c = sorted(''.join(list(str(p[i]) for i in p)))
        return c=='1112'

    def HighCard(self,card):        
        return 0


def problem_54(): #Diamond Club Heart Spade
    d=data.openfile('poker.txt').read().split('\n')
    #log.info(d)
    log.info(len(d))

    s=0         
    for i in d:
        poker(i).win()
    return s
   


               
    
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
            
def problem_57(num=1000):
    from fractions import Fraction
    init = Fraction(1,2)
    n = 0
    for i in range(num-1):
        init = 1/(2 + init)
        #log.info(init+1)
        if len(str((init+1).numerator))>len(str((init+1).denominator)):
            n+=1
    return n

def problem_58(length=None):
    if length:
        for i in range(length):
            pass    

def problem_59(keychars='abcdefghijklmnopqrstuvwxyz',keylen=3):
    ciphertext=list(next(data.openfile('cipher1.txt')).strip().split(','))     
    #ciphertext=encipher('leijiaominabc','zzz')
    #log.info(encipher('leijiaominabc','zzz'))
    #log.info(ciphertext)
    log.info(len(ciphertext))   
    texts = ['',0]
    a,b=divmod(len(ciphertext),keylen)
    for i in itertools.product(keychars,repeat=keylen):        
        cleartext = ''
        space = 0        
        for j in range(a):            
            for k in range(keylen):               
                t = int(ciphertext[keylen*j+k])^ord(i[k])
                if t == ord(' '):
                    space += 1 
                cleartext += chr(t)
        if b:
            for k in range(b):
                t = int(ciphertext[keylen*a+k])^ord(i[k])
                if t == ord(' '):
                    space += 1 
                cleartext += chr(t)
        if space > texts[1]:
            texts[1] = space
            texts[0] = cleartext
    log.info(texts)    
    return sum([ord(i) for i in texts[0]])    

def encipher(texts,key):
    #log.info(texts)
    #log.info(key)
    ciphertext = []
    a,b = divmod(len(texts),len(key))    
    for i in range(a):
        ciphertext += [ord(texts[i*len(key)+j])^ord(key[j]) for j in range(len(key))]
    if b:
        ciphertext += [ord(texts[a*len(key)+j])^ord(key[j]) for j in range(b)]
    return ciphertext

                                   

            
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

        
    
    
    
    