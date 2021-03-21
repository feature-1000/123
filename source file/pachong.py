# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 18:36:06 2020

@author: 10232
"""

import requests
response = requests.get('http://img0.dili360.com/ga/M01/48/3C/wKgBy1kj49qAMVd7ADKmuZ9jug8377.tub.jpg')

with open('1.jpg','wb') as e:
    e.write(response.content)
    e.close()
