"""
- 了解jsonpath模块的使用场景
- 掌握jsonpath模块的使用

1. jsonpath模块的使用使用场景
    若有一个多层嵌套的复杂字典, 想要根据key和下标来批量提取value
     这是较为困难的. jsonpath模块就可以解决这个问题
    jsonpath可以按照key对python字典进行批量数据提取
2. json模块的使用
    jsonpath模块的安装
        pip install jsonpath
    使用
    from jsonpath import jsonpath
    ret = jsonpath(dict, "jsonpath语法规范字符串")

    语法:
     jsonpath               描述
        $                   根节点
        @                   现行节点
        . or []             取子节点
        n/a                 取父节点, jsonpath未支持
        []                  迭代器标识(可以在里面做简单的迭代操作, 例如数组下标, 根据内容选值等)
        [,]                 支持迭代器中做多选
        ?()                 支持过滤操作
        ()                  支持表达式计算
        n/a                 分组jsonpath不支持
    常用语法:
        $                   根节点 -> 最外层的大括号
        .                   子节点
        ..                  内部任意位置, 子孙节点




"""

# 使用
from jsonpath import jsonpath

data = {'key1':{'key2':{'key3':{'key4':{'key5':{'key6':"python"}}}}}}
# 这种多层嵌套的字典
print(data['key1']['key2']['key3']['key4']['key5']['key6'])

# 使用jsonpath模块
# jsonpath的结果为列表, 获取数据所需要的索引
print(jsonpath(data, "$.key1.key2.key3.key4.key5.key6"))

# 快速跨越层级:
print(jsonpath(data, "$..key6")[0]) # 跨越层级的提取

# jsonpath模块的练习



