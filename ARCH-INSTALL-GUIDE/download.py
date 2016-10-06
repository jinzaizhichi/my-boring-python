import os,urllib.request,re,sys,requests,data
print ('欢迎使用arch安装向导获取器')
resp = requests.get("https://raw.githubusercontent.com/redapple0204/my-boring-python/master/tmp/version-beta")
print('目前最新的测试版本是',resp.text)
resp1 = requests.get("https://raw.githubusercontent.com/redapple0204/my-boring-python/master/tmp/version-stable")
print('目前最新的稳定版本是',resp1.text)
print('请输入您要下载的版本（1为测试版，2为稳定版）')
print('将下载到本程序所在的目录')
shuru = input()

if shuru=="1":
	 print('正在下载中.....') 
	 lujing = os.getcwd()
	 os.chdir(lujing)
	 resp3 = requests.get("https://raw.githubusercontent.com/redapple0204/my-boring-python/master/tmp/version-beta-link")
	 data = urllib.request.urlopen(resp3.text).read()
	 with open("arch-install-guide-beta.doc", 'wb') as f:
	  f.write(data)
	  print('下载完毕！请查看本目录生成的arch-install-guide-beta.doc')
if shuru=="2":
	  print('正在下载中....')
	  lujing2 = os.getcwd()
	  os.chdir(lujing2)
	  resp4 = requests.get("https://raw.githubusercontent.com/redapple0204/my-boring-python/master/tmp/version-stable-link")
	  data = urllib.request.urlopen(resp4.text).read()
	  with open("arch-install-guide.doc", 'wb') as f:
	     f.write(data)
	     print('下载完毕！请查看本目录生成的arch-install-guide.doc')


