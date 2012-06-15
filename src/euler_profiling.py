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
    cProfile.run('euler.main()','fooprof')
    p=pstats.Stats('fooprof')
    p.strip_dirs().sort_stats(-1).print_stats()
    #p.sort_stats('name').print_stats()

if __name__=="__main__":    
    #euler_timeit()
    euler_profile()