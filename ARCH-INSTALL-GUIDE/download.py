import os, re, sys, requests, data
from urllib import requests

print ('欢迎使用arch安装向导获取器')
betav = requests.get("https://raw.githubusercontent.com/redapple0204/my-boring-python/master/tmp/version-beta")
print('目前最新的测试版本是', betav.text)
stablev = requests.get("https://raw.githubusercontent.com/redapple0204/my-boring-python/master/tmp/version-stable")
print('目前最新的稳定版本是', stablev.text)
print('请输入您要下载的版本（1为测试版，2为稳定版, 将下载到本程序所在的目录）: ')
cversion = input()
if cversion == "1": 
    filepth = os.getcwd()
    os.chdir(filepth)
    beta_link = requests.get("https://raw.githubusercontent.com/redapple0204/my-boring-python/master/tmp/version-beta-link")
    data = urllib.request.urlopen(beta_link.text).read()
    with open("arch-install-guide.doc", 'wb') as f:
        f.write(data)
if cversion == "2":
    filepth = os.getcwd() # can be same as cversion1
    os.chdir(filepth)
    stable_link = requests.get("https://raw.githubusercontent.com/redapple0204/my-boring-python/master/tmp/version-stable-link")
    data = urllib.request.urlopen(stable_link.text).read()
    with open("arch-install-guide.doc", 'wb') as f:
        f.write(data)
else:
    print("Error: Please enter 1 or 2")
    exit()

