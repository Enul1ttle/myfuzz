### 收集的一些不错的字典
之前发现去重后，还是有重复，原因是合并的字典不统一，有的dir带/,有的不带。写了个小脚本统一去掉每行首个/后，DIR0x01减少了近10万条重复

```
DIR0x01.txt  #超全目录字典

WebShell-Password.txt #webshell 密码
Webmanage-Username.txt # web后台管理用户名

NewMimi.txt       #高效密码字典  来自klionsec
NewNormal.txt
```
#### 2019/7/14 
有时候目录太大并不是一件好事，经常把对方网站扫蹦，我在想能不能像密码字典一样来个TOP1000。趁着周末时间，我先把猪猪侠字典、7kbscan、kali 目录字典，御剑珍藏版、fuzzDicts等众多目录字典合成一个，共480W条数据。本来想按重复次数排序，无奈电脑性能太差，蓝屏几次都没跑完。然后只能通过python把重复超过三次的数据提取出来。就有了php.txt、asp.txt、jsp.txt 三个文件。里面都已经包含了dir和html，爆破的时候选一个字典就够了，其中aspx包含在asp.txt中。
```
高效的目录字典
dirtop10w.txt    在480w条目录字典中出现超5次
dirtop15000.txt  在480w条目录字典中出现超15次
dirtop9300.txt   在480w条目录字典中出现超过20次

```
#### 2019/7/17 python3根据网站域名生成字典
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
run(url)

tempList = []

for key in keyList:
	for suff in suffixList:
		tempList.append(key + suff)

fobj = open("keyFiles.txt" , 'w')
for each in tempList:
    fobj.write('%s%s' % (each,'\n'))
    fobj.flush()
#将dirtop9300.txt 加入
f= open('dirtop9300.txt','r',encoding='UTF-8')
for s in f.readlines():
	fobj.write(s)

print('OK!')
```
