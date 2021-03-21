# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:01:01 2020

@author: 10232
"""

import http.cookiejar,urllib.request
filename = "cookie.txt"
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com/')
cookie.save(ignore_discard=True,ignore_expires=True)

response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))
