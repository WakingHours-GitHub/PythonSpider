"""
在chrome59后, 可以变成无头浏览器. 也就是不显示浏览器界面
对应:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # 添加到创建Driver对象
    chrome = webdriver.Chrome(chrome_options=options)







"""
from selenium import webdriver
from selenium.webdriver.common.by import By


def firefox_headless():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    fox = webdriver.Firefox(options=options)
    fox.get('http://www.baidu.com')
    print(fox.page_source)


def chrome_headless():
    # 创建选项对象
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # 添加到
    chrome = webdriver.Chrome(chrome_options=options)
    chrome.get('http://www.baidu.com')
    html = chrome.page_source
    print(html)




def firefox_test():
    fox = webdriver.Firefox() # 创建浏览器请

    fox.get("https://cn.bing.com/?mkt=zh-CN") # 地址栏请求

    # 在查找时, 我们都是通过元素特征来去定位标签, 如果没有找到则会报错, 因此在寻找元素时, 一定要保证能够找到
    # 并且浏览器加载资源是需要时间的. 这种我们只能等待一会
    fox.find_element(By.ID, value="sb_form_q").send_keys("python")
    # 标签.send_keys(内容)就表示输入内容



    fox.find_element(By.ID, value="search_icon").click()

if __name__ == '__main__':
    # chrome_headless()
    firefox_headless()
