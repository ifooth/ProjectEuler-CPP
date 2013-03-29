'''
Created on 2012-7-18

@author: Joe Lei
'''
from euler.problem import problem_1_25
from euler.problem import problem_26_50
from euler.problem import problem_51_75
from euler.problem import problem_76_100
from euler.problem import problem_101_125
class Problem():
    
    def __init__(self,problem_num):
        self.problem_num=problem_num
        assert type(self.problem_num) is type(1),"Problem Init must a Integer"
        
    
    def run(self):
        assert self.problem_num>0,"Problem num must a Positive Integer"
        str_pro="problem_"+str(self.problem_num)+"()" 
        if self.problem_num<25:                              
            return exec("print(problem_1_25."+str_pro+")")            
        elif self.problem_num<50:                       
            return exec("print(problem_26_50."+str_pro+")")
        elif self.problem_num<75:                       
            return exec("print(problem_51_75."+str_pro+")")
        elif self.problem_num<100:                       
            return exec("print(problem_76_100."+str_pro+")")
        elif self.problem_num<125:                       
            return exec("print(problem_101_125."+str_pro+")")
            