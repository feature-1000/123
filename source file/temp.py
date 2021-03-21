# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 10:46:40 2020

@author: 10232
"""
def p(number=3,true_word='12345'):
    while number > 0:
        password = input('password : ')
        if password == true_word:
            print('successful !')
            break
        else:
            print('wrong again')
            number -= 1
    else:
        print('Your account has been suspended !')
        
p(number=3)        
        