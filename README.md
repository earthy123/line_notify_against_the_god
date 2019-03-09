# LINE Notify for Against the God Novel!

This project was created for serving who wants to read latest chapter of the novel but don't know when it will be posted on the website so they have to checking by thier own. To aviod of waste of time. LINE Notify will tell it for you when the new chapter come. More detail about the novel [link](https://www.kawebook.com/story/70/%E0%B8%99%E0%B8%B4%E0%B8%A2%E0%B8%B2%E0%B8%A2/%E0%B8%99%E0%B8%B4%E0%B8%A2%E0%B8%B2%E0%B8%A2-%E0%B8%88%E0%B8%B5%E0%B8%99-%E0%B8%81%E0%B8%B3%E0%B8%A5%E0%B8%B1%E0%B8%87%E0%B8%A0%E0%B8%B2%E0%B8%A2%E0%B9%83%E0%B8%99-%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B9%80%E0%B8%8B%E0%B8%B5%E0%B8%A2%E0%B8%99/%E0%B8%AD%E0%B8%AA%E0%B8%B9%E0%B8%A3%E0%B8%9E%E0%B8%A5%E0%B8%B4%E0%B8%81%E0%B8%9F%E0%B9%89%E0%B8%B2-Against-the-Gods)


## Prerequisites


### Required libraries
  - Python 2.7
  - Pip
  - Chromium
  - ChromeDiver
  - BeautifulSoup4
  - Requests.

### HOW TO INSTALL
#### ** Set Chrome version**
```
CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`
```
#### **Remove existing downloads and binaries so we can start from scratch**
```
sudo apt-get remove google-chrome-stable
rm ~/selenium-server-standalone-*.jar
rm ~/chromedriver_linux64.zip
sudo rm /usr/local/bin/chromedriver
sudo rm /usr/local/bin/selenium-server-standalone.jar
```
#### **Install dependencies**
```
sudo apt-get update
sudo apt-get install -y unzip openjdk-8-jre-headless xvfb libxi6 libgconf-2-4
```
#### **Install Chromium**
```
sudo apt install -y chromium-browser
```
#### **Install ChromeDriver**
```
wget -N http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip -P ~/
unzip ~/chromedriver_linux64.zip -d ~/
rm ~/chromedriver_linux64.zip
sudo mv -f ~/chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod 0755 /usr/local/bin/chromedriver
```
#### **Install Pip**
```
sudo apt install python-pip -y
```

#### **Install Selenium**
```
python -m pip install -U selenium
```
#### **Install BeautifulSoup4.**
```
sudo apt-get install python-bs4 -y
```
#### **Install Requests**
```
pip install requests
```
## Try it!
```
Read it on example.ipynb
```
