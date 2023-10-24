"""
json 实质上就是一个字符串, 里边包含的是py的列表或者字典
列表内的元素为字典
"""

import json

# 通过dumps()可以把数据转换为json格式
data = [{"name": "clb", "age": 22}, {"name": "zzy", "age": 21}, {"name": "zly", "age": 34}]

data_json = json.dumps(data, ensure_ascii=False) # ensure_ascii=False 确保中文可以正确显示,不转化为ascii码值
print(type(data_json))
print(data_json)

stu = {"name": "gl", "age": 23}
print(type(stu))
stu_json = json.dumps(stu)
print(stu_json)

# 通过loads()可以把数据从json转化为py格式
s = '[{"name": "clb", "age": 22}, {"name": "zzy", "age": 21}, {"name": "zly", "age": 34}]'
l = json.loads(s)
print(type(l))
print(l)

s = '{"name": "gl", "age": 23}'
d = json.loads(s)
print(type(d))
print(d)
