'''
Created on May 26, 2012

@author: Joe Lei
'''

import logging
import logging.config

logging.config.fileConfig('../etc/logging.ini')

log=logging.getLogger('ProjectEuler')

import euler.problem.problem as p

def main():        
    p.Problem(51).run()
    
if __name__=="__main__":    
    main()     
    
    
    
    