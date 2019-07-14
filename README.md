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
