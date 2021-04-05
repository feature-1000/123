#!/usr/bin/env python
# coding: utf-8

# In[21]:


from selenium import webdriver
from selenium.webdriver import ActionChains
from  requests.cookies import  RequestsCookieJar
import  requests
import time
import datetime
browser = webdriver.Chrome()     # 打开
                          


# In[10]:


import datetime
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
now


# In[6]:


def login():
    # 打开淘宝首页，通过扫码登录
    browser.get("https://www.taobao.com/")
    time.sleep(3)
    # 打开登录界面
    find_login = browser.find_element_by_link_text("亲，请登录")
    if find_login:
        find_login.click()
        print("请扫码登录")
        time.sleep(10)
        
#login()


# In[7]:


# 选择购物车列表
def picking(method):
    # 是否全选购物车
    if method == 0:
        while True:
            try:
                if browser.find_element_by_id("J_SelectAll1"):
                    browser.find_element_by_id("J_SelectAll1").click()
                    print('全选购物车成功')
                    break
            except:
                print(f"找不到购买按钮")
    else:
        print(f"请手动勾选需要购买的商品")
        time.sleep(1)
#picking(0)  


# In[8]:


# 点击结算按钮
def settlement():
    while True:
        try:
            if browser.find_element_by_id('J_SelectedItemsCount').text >= '1':
                browser.find_element_by_link_text("结 算").click()
                print(f"结算成功，准备提交订单")
                break
        except:
            pass
#settlement()


# In[9]:


# 点击提交订单按钮
def submitting():
    while True:
        try:
            if browser.find_element_by_link_text('提交订单'):
                browser.find_element_by_link_text('提交订单').click()
                print(f"抢购成功，请尽快付款")
                break
        except:
            print(f"再次尝试提交订单")
#submitting()


# In[10]:


def run(times):
    # 打开购物车列表页面
    print('正在抢购！')
    browser.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now > times:
            # 全选购物车
            picking(0)
            # 点击结算按钮
            settlement()
            # 提交订单
            submitting()
            print(now)
            browser.close()
            break


# In[22]:


run('2021-04-05 20:40:55')


# In[ ]:




