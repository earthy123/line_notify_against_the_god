
# coding: utf-8

# In[10]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import requests
import time
import os


# In[11]:


file_name = 'against_the_god_lastest_ch.txt'
current_path =os.getcwd()
url ='https://notify-api.line.me/api/notify'
# authen = 'Bearer YOUR TOKEN'

authen = 'Bearer Your token'


# In[3]:


def send_noti(URL,Authorization,text):
    r = requests.post(URL,headers={'Authorization': Authorization}, data = {'message':text})


# In[4]:


victim_url ="https://www.kawebook.com/story/70/%E0%B8%99%E0%B8%B4%E0%B8%A2%E0%B8%B2%E0%B8%A2/%E0%B8%99%E0%B8%B4%E0%B8%A2%E0%B8%B2%E0%B8%A2-%E0%B8%88%E0%B8%B5%E0%B8%99-%E0%B8%81%E0%B8%B3%E0%B8%A5%E0%B8%B1%E0%B8%87%E0%B8%A0%E0%B8%B2%E0%B8%A2%E0%B9%83%E0%B8%99-%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B9%80%E0%B8%8B%E0%B8%B5%E0%B8%A2%E0%B8%99/%E0%B8%AD%E0%B8%AA%E0%B8%B9%E0%B8%A3%E0%B8%9E%E0%B8%A5%E0%B8%B4%E0%B8%81%E0%B8%9F%E0%B9%89%E0%B8%B2-Against-the-Gods"


# In[9]:





# In[13]:


options = webdriver.ChromeOptions()
options.add_argument('headless')
# browser = webdriver.PhantomJS()
browser = webdriver.Chrome(executable_path=current_path+'/chromedriver',chrome_options=options)
browser.get(victim_url)


# In[14]:


timeout = 10
try:
    WebDriverWait(browser,timeout).until(EC.visibility_of_element_located((By.XPATH,"//*[text()='รีวิว']")))
except TimeoutException:
    print("timeout wait page for load")
    browser.quit()


# In[19]:


html = browser.page_source
soup = BeautifulSoup(html, "lxml")
pos = soup.find_all(class_="purple-color-light")[-1]


# In[20]:


current_ch =str.strip(pos.get_text())


# In[17]:


if os.path.isfile(file_name)!=True:
    previous_ch=''
    with open(file_name,'w') as f:
        f.write('')
else:
    with open(file_name,'r') as f:
        previous_ch = f.read()


# In[18]:


if previous_ch!=current_ch:
    text='ตอนใหม่ :'+current_ch
    send_noti(url,authen,text)
    with open(file_name,'w') as f:
        f.write(current_ch)
else:
    text='ยังไม่มีตอนใหม่'
    send_noti(url,authen,text)
    
print('done')

