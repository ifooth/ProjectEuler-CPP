'''
Created on Jun 6, 2012

@author: Administrator
'''
from collections import Counter
class lib_euler_poker():
    '''
    classdocs
    '''


    def __init__(self,cards):
        '''
        Constructor
        '''
        self.examine_cards(cards)
    d = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, \
         '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, \
         'K': 13, 'A': 14, 'One Pair': 29, 'Two Pairs': 59, \
         'Three of a Kind': 74, 'Straight': 89, 'Flush': 104, \
         'Full House': 119, 'Four of a Kind': 134,\
         'Straight Flush': 149, 'Royal Flush': 164}
    
    