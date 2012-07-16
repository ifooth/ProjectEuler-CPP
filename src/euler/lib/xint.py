'''
Created on 2012-7-16

@author: botwave
'''
import collections

class xint(int):
    '''
    classdocs
    '''       
    def isPrime(self):
        assert self > 1, "I must be a positive integer"
        if self < 2:return False
        elif self == 2:return True
        elif not self & 1:return False
        elif any((self % i) == 0 for i in range(3, int(self ** 0.5) + 1, 2)):return False
        return True
    def nextPrime(self):
        if self&1:
            a=self+2
        else:a=self+1    
        while(not xint(a).isPrime()):
            a+=2
        return a
        
    def isPalindromic(self):
        return str(self) == str(self)[::-1]
    def factors_temp(self):
        yield 1
        i, limit = 2, self ** 0.5
        while i <= limit:
            if self % i == 0:
                yield i
                self //= i
                limit = self ** 0.5
            else:i += 1
        if self > 1:yield self
        
    def factors(self): 
        cnt=collections.Counter()
        for j in list(self.factors_temp()):
            cnt[j]+=1
        return dict(cnt)
    
    def sumOfDivisors(self):
        """
        counts the number of positive integers less than or equal to n that are relatively prime to n 
        """
        assert self>0,"I must be a positive integer and must be exceed 1"
        if self==1:return 0
        i_sum=1
        for key,value in self.factors().items():
            i_sum*=sum(key**i for i in range(value+1))
        return i_sum//2-self
    
    def numberOfDivisors(self):
        """
        number of divisors
        """
        assert self>0
        if self==1:return 1
        else:i_sum=1
        for value in self.factors(self).values():
            i_sum*=(value+1)
        return i_sum//2
    
    def phi(self):
        i_result=1
        d_temp=self.factors()
        d_temp.pop(1)
        for key,value in d_temp.items():
            i_result*=(key**value-key**(value-1))
        return i_result
    def divisors(self):
        l_temp=self.factors()
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
            j=1
            l_result=l_a[0]
            while j<len(l_a):
                l_te=[]
                for t_m in l_a[j]:
                    for t_n in l_result:
                        l_te.append(t_m*t_n)
                        l_result=l_te
                        j+=1
        return l_result
