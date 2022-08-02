import gc
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

fox = webdriver.Firefox()
url = "https://www.huya.com/g/lol"

fox.get(url)
page = 1
while True:
    print("正在打印第" + page.__str__() + "页") #
    sleep(1) # 有时候刷新太快, 我们需要等待浏览器渲染. 然后再接下来的操作
    html_source_code = fox.page_source

    # print(html_source_code)

    # 我们要获取主播的名字以及观看人数
    # 这里我们使用find_elements()
    name_list = fox.find_elements(By.XPATH, '//i[@class="nick"]')
    count_list = fox.find_elements(By.XPATH, '//i[@class="js-num"]')

    # 遍历
    for index, content in enumerate(zip(name_list, count_list)):
        name, count = content
        print(index, ':', name.text, ",", count.text)  # 使用text取标签中的内容

    # 然后进行翻页. 一直下一页, 然后使用try-except,
    # 如果能够找到, 则继续下一页, 如果找不到则说明已经是最后一页, 则退出
    # 如果最后一页中, 下一页标签还在, 那么我们就要换别的方式去判断了
    page += 1
    # 这是一种判断方式
    try:
        # 点击下一页.
        fox.find_element(By.XPATH, '//a[@class="laypage_next"]').click()
    except Exception:
        # 如果出现异常, 则表示已经是最后一页
        print("已经是最后一页, 退出")
        break

    # 还有一种判断方式, 判断标签属性是否是disable,




fox.quit()

gc.collect()  # 收集垃圾
