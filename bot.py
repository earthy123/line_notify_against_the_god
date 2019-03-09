
#!/usr/bin/env python
# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import requests
import time
import os
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# In[51]:


th_file_name = 'against_the_god_lastest_ch.txt'
eng_file_name = 'against_the_god_lastest_ch_eng.txt'
current_path =os.getcwd()
line_url ='https://notify-api.line.me/api/notify'
authen = 'Bearer YOUR TOKEN'
eng_url ="https://lnmtl.com/novel/against-the-gods"
th_url ="https://www.kawebook.com/story/70/%E0%B8%99%E0%B8%B4%E0%B8%A2%E0%B8%B2%E0%B8%A2/%E0%B8%99%E0%B8%B4%E0%B8%A2%E0%B8%B2%E0%B8%A2-%E0%B8%88%E0%B8%B5%E0%B8%99-%E0%B8%81%E0%B8%B3%E0%B8%A5%E0%B8%B1%E0%B8%87%E0%B8%A0%E0%B8%B2%E0%B8%A2%E0%B9%83%E0%B8%99-%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B9%80%E0%B8%8B%E0%B8%B5%E0%B8%A2%E0%B8%99/%E0%B8%AD%E0%B8%AA%E0%B8%B9%E0%B8%A3%E0%B8%9E%E0%B8%A5%E0%B8%B4%E0%B8%81%E0%B8%9F%E0%B9%89%E0%B8%B2-Against-the-Gods"


# In[3]:


th_xpath = "//*[text()='รีวิว']"
eng_xpath = "//*[@id=\"app\"]/main/div[2]/div/div[1]/div[1]/div/h3"


# In[4]:


def send_noti(URL,Authorization,text):
    r = requests.post(URL,headers={'Authorization': Authorization}, data = {'message':text})


# In[9]:


def get_component(URL,X_PATH):
    timeout = 10
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--incognito")
    browser = webdriver.Chrome('/usr/local/bin/chromedriver',options=options)
    browser.get(URL)
    
    
    try:
        WebDriverWait(browser,timeout).until(EC.visibility_of_element_located((By.XPATH,X_PATH)))
    except TimeoutException:
        print("timeout wait page for load")
        browser.quit()
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    return soup


# In[40]:


def load_prev(FILE_NAME):
    if os.path.isfile(FILE_NAME)!=True:
        previous_ch=''
        with open(FILE_NAME,'w') as f:
            f.write('')
    else:
        with open(FILE_NAME,'r') as f:
            previous_ch = f.read()
    
    return previous_ch
#     print('done at: ',datetime.datetime.now())


# In[69]:


def check_new_chapter(P_CH,C_CH,FILE_NAME,AUTHEN):
    if P_CH!=C_CH:
        text=' '+C_CH
        send_noti(line_url,AUTHEN,text)
        with open(FILE_NAME,'w') as f:
            f.write(C_CH)
    else:
        text='ยังไม่มีตอนใหม่'
        send_noti(line_url,AUTHEN,text)
    print('CH: ',C_CH)
    print('done at: ',datetime.datetime.now())


# In[70]:


th_soup =get_component(th_url,th_xpath)
eng_soup =get_component(eng_url,eng_xpath)


# In[71]:


th_component =th_soup.find_all(class_="purple-color-light")[-1]
th_current_ch =th_component.get_text().strip()


# In[72]:


eng_component = eng_soup.find_all(class_="badge chapter-badge")[0]
eng_current_ch =eng_component.get_text().strip()


# In[73]:


th_previous_ch = load_prev(th_file_name)
check_new_chapter(th_previous_ch,th_current_ch,th_file_name,authen)


# In[74]:


eng_previous_ch = load_prev(eng_file_name)
check_new_chapter(eng_previous_ch,eng_current_ch,eng_file_name,authen)

