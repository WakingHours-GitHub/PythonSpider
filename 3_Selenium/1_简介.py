"""
selenium是一个Web自动化测试工具, 最初是为网站测试而开发的,
selenium自己本身不是一个浏览器, 他无法直接访问, selenium通过driver与浏览器沟通
Python3使用的浏览器
    firefox gechodriver
    chromeDriver
    找到对应相应的版本, 然后将driver放在python解释器的主目录

如何使用selenium


"""

from selenium import webdriver
firefox = webdriver.Firefox() # 前提, 需要能够找到驱动

firefox.get("https://baidu.com") # 发送亲贵


# 获取渲染后的页面源代码
print(firefox.page_source)

firefox.save_screenshot('') # 保存图片



firefox.quit() # 执行完毕直接退出

