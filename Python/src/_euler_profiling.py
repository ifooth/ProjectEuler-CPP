'''
Created on Jun 12, 2012

@author: Administrator
'''
import cProfile
import pstats
import timeit
import _euler


def euler_timeit():
    print(timeit.Timer(lambda:_euler.main()).timeit(1))    
    
def euler_profile():
    cProfile.run('_euler.main()')
if __name__=="__main__":    
    euler_timeit()
    #euler_profile()
    import time
    for i in range(10,1000):
        