"""
面向对象,数据分析案例
实现步骤:
1. 设计一个类,可以完成数据的封装
2. 设计一个抽象类,定义文件读取的相关功能,并使用子类实现具体功能
3. 读取文件,生产数据对象
4. 尽享数据需求的逻辑计算(计算每一天的销售额)
5. 通过PyEcharts进行图形绘制
"""

from data_define import Record
from file_define import TextFileReader, JsonFileReader
from pyecharts.charts import Bar
from pyecharts.options import *

text_file_reader = TextFileReader("one.txt")
json_file_reader = JsonFileReader("two.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
# 将两个月的数据合并到一起
all_data: list[Record] = jan_data + feb_data

# 开始进行数据计算
data_dict = {}
for recoder in all_data:
	if recoder.date in data_dict.keys():
		# 如果当前日期存在, 对其所对应的money进行累计
		data_dict[recoder.date] += recoder.money
	else:
		data_dict[recoder.date] = recoder.money

# 可视化图标开发
bar = Bar()
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()))

bar.render('销售记录.html')
