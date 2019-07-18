### 合并提取的高效目录字典
合并SaiDict、fuzzDicts、Dirpath、SecLists、7kbscan、御剑等目录字典，再通过python把重复率高的提取出来。比如dirtop10000.txt 在600W条数据中，重复出现达20次。



### 收集的一些不错的字典

```

WebShell-Password.txt #webshell 密码
Webmanage-Username.txt # web后台管理用户名

NewMimi.txt       #高效密码字典  来自klionsec
NewNormal.txt
```

#### 2019/7/17 dir.py根据网址生成字典
不知再哪找的源码，修改了一下
```

#coding=utf-8
# python3.6
import sys
import imp
imp.reload(sys)

import os
import os.path
import time
time1 =time.time()

suffixList = ['.rar','.zip','.sql','.gz','.tar','.ba2','.tar.bz2','.bak','.dat','.txt','.mdb','.doc','.lst','.tmp','.temp','.xml']

keyList = ['web','webroot','WebRoot','website','www','wwww','www1','www2','www3','www4','www5','default','log','elk','weblog',
'mysql','ftp','FTP','MySQL','redis','Redis','sa','cig','access','error','logs','data','database','sql','vpn','proxy','temp',]


def run(url):
	# 根据URL，推测一些针对性的文件名
	num1 = url.find('.')
	num2 = url.find('.', num1 + 1)
	keyList.append(url[num1 + 1:num2])
	keyList.append(url[num1 + 1:num2].upper())
	keyList.append(url)  # 如www.hack.com
	keyList.append(url.upper())
	keyList.append(url.replace('.', '_'))  # www_hack_com
	keyList.append(url.replace('.', '_').upper())
	keyList.append(url.replace('.', ''))  # wwwhackcom
	keyList.append(url.replace('.', '').upper())
	keyList.append(url[num1 + 1:])  # hack.com
	keyList.append(url[num1 + 1:].upper())
	keyList.append(url[num1 + 1:].replace('.', '_'))  # hack_com
	keyList.append(url[num1 + 1:].replace('.', '_').upper())


print ("Please input (e.g:www.hack.com):")
url = input()
script = int(input("输入数字选择脚本 1 asp、2 aspx、3 php、4、jsp: "))
run(url)

tempList = []

for key in keyList:
	for suff in suffixList:
		tempList.append(key + suff)

fobj = open("keyFiles.txt" , 'w')
for each in tempList:
    fobj.write('%s%s' % (each,'\n'))
    fobj.flush()
if script == 1:
	f= open('./dic/asp.txt','r',encoding='gbk')
	for s in f.readlines():
		fobj.write(s)
if script == 2:
	f= open('./dic/aspx.txt','r',encoding='gbk')
	for s in f.readlines():
		fobj.write(s)
if script == 3:
	f= open('./dic/php.txt','r',encoding='gbk')
	for s in f.readlines():
		fobj.write(s)
if script == 4:
	f= open('./dic/jsp.txt','r',encoding='gbk')
	for s in f.readlines():
		fobj.write(s)



f= open('./dic/dir.txt','r',encoding='gbk')
for s in f.readlines():
	fobj.write(s)


print('OK!')
```
项目地址：https://github.com/Enul1ttle/Python3Lean/tree/master/%E6%A0%B9%E6%8D%AE%E7%BD%91%E5%9D%80%E7%94%9F%E6%88%90%E7%9B%AE%E5%BD%95%E7%88%86%E7%A0%B4%E5%AD%97%E5%85%B8    
#### 部分字典生成效果
![image](https://raw.githubusercontent.com/Enul1ttle/Python3Lean/master/%E6%A0%B9%E6%8D%AE%E7%BD%91%E5%9D%80%E7%94%9F%E6%88%90%E7%9B%AE%E5%BD%95%E7%88%86%E7%A0%B4%E5%AD%97%E5%85%B8/dir.png)
