"""
JSON与JsonPATH:

JsonPath专门针对Json格式的数据.
json: 简单就是说javascript中的对象和数组, 所以这两种结构就是对象和数组两种结构
    对象: 就是{}, 数据结构: {key: value, ...}, 使用key取value
    数组: 就是[], 数据结构: [ele1, ele2, ...], 使用索引取值




python中的json模块:
    四个功能: dumps, dump, loads, load 用于字符串和python数据类型之间的转换
    json.loads() 将json字符串转换对应的python对象
    json.dumps() 将python类型转换为json字符串

    json.dump() 将python内置类型序列化为json对象后写入文件
    json.load() 读取文件中的json形式的字符串 转换为python类型

jsonPath:
    安装: pip install jsonpath

jsonpath语法:
    XPath	  JSONPath	  Description
    /	        $	        根元素
    .	        @	        当前元素
    /	        . or []	    子元素
    ..	        n/a	        父元素
    //	        ..	        递归下降，表示相对定位(直接定位key)
    *	        *	        通配符，表示所有的元素
    @	        n/a	        属性访问字符
    []	        []	        子元素操作符
                [,]	        连接操作符在XPath 结果合并其它结点集合。JSONP允许name或者数组索引。
    n/a	        [start: end: step]	数组分割操作从ES4借鉴。
    []	        ?()	        应用过滤表示式
    n/a	        ()	        脚本表达式，使用在脚本引擎下面。
    ()	        n/a(没有)    Xpath分组


"""
import requests
from fake_useragent import UserAgent
import json #

from jsonpath import jsonpath # jsonpath函数,



str = '{"name": "盗梦空间"}' # 最简单的一个json字符串
print(type(str)) # <class 'str'>

# 转换成json对象
json_obj = json.loads(str)
print(json_obj) # {'name': '盗梦空间'}
print(type(json_obj)) # <class 'dict'>

json_str = json.dumps(json_obj)
print(json_str) # {"name": "\u76d7\u68a6\u7a7a\u95f4"} # 使用uncode编码

# 关闭转换ASCi2码转换
json_str = json.dumps(json_obj, ensure_ascii=False)
print(json_str)
print(type(json_str)) # <class 'str'>

# 序列化到文件
json.dump(json_obj, open("movie.txt", 'w', encoding='utf-8'),  ensure_ascii=False)


file_json_str = json.load(open("movie.txt", encoding='utf-8'))
print(file_json_str) # {'name': '盗梦空间'}

# 练习
url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
# 去到json.cn进行解析.

headers = {
    "User-Agent": UserAgent().random
}

# 发送请求
resp = requests.get(url, headers=headers)

print(resp.text) # 很显然就是json格式的字符串

# 转换成json对象(python中是字典和列表)
json_obj = json.loads(resp.text)
codes = jsonpath(json_obj, "$..code") # 必须要从根开始找, 然后使用相对路径直接找到对应key
# 除此之外, resp可以直接返回页面为json格式
names = jsonpath(resp.json(), "$..name")
print(names)
print(codes)




