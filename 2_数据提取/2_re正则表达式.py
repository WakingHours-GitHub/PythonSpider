"""




常用方法:
    re.match: 从字符串起始位置匹配一个pattern(模式), 如果不是起始位置匹配成功的话, match()就返回None
        re.match(pattern, string, flags=0)
    re.search:



"""

import re

str1 = "I Study Python3.6 Everyday"

print("-" * 20 + "match()" + "-" * 20)
# 匹配第一个字符:
m1 = re.match(r"I", str1)  # I
m2 = re.match(r'\w', str1)  # I
# m3 = re.match()


# 搜索study
# re.search(): 搜索, 全局搜索, 匹配到第一个停止.
# m7 = re.match(r'Study', str1) # 找不到, 一位内match是从左(头)开始匹配的.
# print(m7.group()) # AttributeError: 'NoneType' object has no attribute 'group'
print(m2.group())

print("-" * 20 + "search()" + "-" * 20)
s1 = re.search(r'Study', str1)  # Study
s2 = re.search(r'S\w+', str1)  # Study

print(s2.group())

# 匹配python3.6
s3 = re.search(r'P\w+.\d', str1)  # Python3.6
print(s3.group())

# findall()
print("-" * 20 + "findall()" + "-" * 20)

# 匹配所有的y
f1 = re.findall(r'y', str1)  # 返回一个列表.
print(f1)  #

# 练习
str2 = "<div><a href='http://www.bjsxt.com'>尚学堂bjsxt</a></div>"
t1 = re.findall(r'[\u4e00-\u9fa5]\w+', str2)  # ['尚学堂bjsxt']
# 但是这样很不容易理解, 所以在开发中, 我们一般都使用贪婪
t2 = re.findall(r"<a href='http://www.bjsxt.com'>(.+)</a>", str2)
print(t2)  # ['尚学堂bjsxt']
t3 = re.findall(r"<a href='(.+)'>", str2)
print(t3)  # ['http://www.bjsxt.com']
# .是匹配任意字符(除\n), 然后+是多个字符, 因此就将标签内中的文字匹配出来了.

# sub() 替换
# 把dir换成span标签
# sub(正则, 替换, 字符串)
su1 = re.sub(r'<div>(.+)</div>', r'<span>\1<\span>', str2)
print(su1)



