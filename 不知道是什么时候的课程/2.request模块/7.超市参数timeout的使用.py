# 超时参数timeout的使用
# timeout就是请求没有结果时候的等待时间
# 如果按照默认是180s, 这个时间是非常长的, 也就导致了我们的效率非常低
# 所以我们需要修改timeout参数
import requests

# 使用方法:
# resp = requests.get(url, timeout=) # 直接设置1timeout参数
# 发送请求后, timeout值之内返回响应, 否则就抛出异常
url = "https://twitter.com"

resp = requests.get(url, timeout=3) # 接收到响应的时间 >= 3 时, 则报异常








