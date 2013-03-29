'''
Created on May 26, 2012

@author: Joe Lei
'''

import logging
import logging.config

logging.config.fileConfig('../etc/logging.ini')
log=logging.getLogger('euler')

from problems import Problem
    
if __name__=="__main__":    
    result=Problem(51).run()
    log.info(result)     
    
    
    
    