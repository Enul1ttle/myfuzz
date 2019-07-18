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