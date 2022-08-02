"""

selenium滚动条的使用:
    因为有一些页面只显示页面显示的内容, 未显示的内容就不渲染,
    此时find_element就找不到标签, 因此我们需要使用滚动条提前渲染.

    但是selenium无法定位到滚动条元素, 因此我们需要借助JS来实现屏幕滚动
    driver.execute_script(js语句)

selenium处理滚动条:
    js = "var q=document.getElementById('id').scrollTop=0" # 滚动到最顶部
    js = ... .scrollTop=10000" # 10000是最底部
    js = "var q=document.body.scrollTop=0" # 在Chrome中管用.

    # 向下滚动500个像素
    driver.execute_script('window.scrollBy(0,500)')
    # 向上滚动500个像素
    driver.execute_script('window.scrollBy(0,-500)')
    # 向右滚动500个像素
    driver.execute_script('window.scrollBy(500,0)')
    # 向左滚动500个像素
    driver.execute_script('window.scrollBy(-500,0)')

    # 滚动至元素可见，这个经常用
    driver.execute_script("arguments[0].scrollIntoView();", ele)
    



"""





