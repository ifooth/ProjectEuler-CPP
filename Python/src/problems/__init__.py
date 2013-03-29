'''
Created on 2012-7-18

@author: Joe Lei
'''

__all__=["problem_1_25","problem_26_50","problem_51_75","problem_76_100",\
         "problem_101_125","problem_125_150","problem_151_175","problem_176_200"]         

from problems import problem_1_25
from problems import problem_26_50
from problems import problem_51_75
from problems import problem_76_100
from problems import problem_101_125
import logging
log=logging.getLogger(__name__)
class Problem():
    
    def __init__(self,problem_num):
        self.problem_num=problem_num
        assert type(self.problem_num) is type(1),"Problem Init must a Integer"
        
    
    def run(self):
        assert self.problem_num>0,"Problem num must a Positive Integer"
        str_pro="problem_%s()"%self.problem_num 
        if self.problem_num<25:                              
            return exec("problem_1_25.%s"%str_pro)            
        elif self.problem_num<50:                       
            return exec("problem_26_50.%s"%str_pro)
        elif self.problem_num<75:
            log.info(exec("problem_51_75.%s"%str_pro))
            return exec("problem_51_75.%s"%str_pro)            
        elif self.problem_num<100:            
            return exec("problem_76_100.%s"%str_pro)
        elif self.problem_num<125:                       
            return exec("problem_101_125.%s"%str_pro)
            


        
    
        