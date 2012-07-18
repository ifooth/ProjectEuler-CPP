'''
Created on Jun 12, 2012

@author: Administrator
'''
import cProfile
import pstats
import timeit
import euler


def euler_timeit():
    print(timeit.Timer(lambda:euler.main()).timeit(1))    
    
def euler_profile():
    cProfile.run('euler.main()')
if __name__=="__main__":    
    #euler_timeit()
    euler_profile()