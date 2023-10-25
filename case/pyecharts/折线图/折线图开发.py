"""
折线图开发
"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, ToolboxOpts, LegendOpts, VisualMapOpts, LabelOpts

# 处理数据
f_us = open("./美国.txt", "r", encoding="UTF-8")
f_india = open("./印度.txt", "r", encoding="UTF-8")
f_jp = open("./日本.txt", "r", encoding="UTF-8")

# 读取文件内的数据
us_data = f_us.read()  # 美国数据的所有内容
india_data = f_india.read()
jp_data = f_jp.read()

# 对数据不合json规范的头处理
us_data = us_data.replace('jsonp_1629344292311_69436(', "")
india_data = india_data.replace('jsonp_1629350745930_63180(', "")
jp_data = jp_data.replace('jsonp_1629350871167_29498(', "")

# 对数据不合json的尾处理
us_data = us_data[:-2]
india_data = india_data[:-2]
jp_data = jp_data[:-2]

# json转py字典
us_dict = json.loads(us_data)
india_dict = json.loads(india_data)
jp_dict = json.loads(jp_data)

# 获取trend key
us_trend_data = us_dict['data'][0]['trend']
india_trend_data = india_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
print(us_trend_data)

# 获取日期数据,用于x轴
us_x_data = us_trend_data['updateDate'][:314]
india_x_data = india_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]

# 获取确诊数据,用于y轴
us_y_data = us_trend_data['list'][0]['data'][:314]
india_y_data = india_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]

# 获取治愈数据,用于y轴
us_y_data_zy = us_trend_data['list'][1]['data'][:314]
india_y_data_zy = india_trend_data['list'][1]['data'][:314]
jp_y_data_zy = jp_trend_data['list'][1]['data'][:314]

# 获取死亡数据,用于y轴
us_y_data_sw = us_trend_data['list'][2]['data'][:314]
india_y_data_sw = india_trend_data['list'][2]['data'][:314]
jp_y_data_sw = jp_trend_data['list'][2]['data'][:314]

# 获取新增确诊数据,用于y轴
us_y_data_xz = us_trend_data['list'][3]['data'][:314]
india_y_data_xz = india_trend_data['list'][3]['data'][:314]
jp_y_data_xz = jp_trend_data['list'][3]['data'][:314]

# 创建一个折线图对象
line = Line()

# 给折线图添加x轴对象
line.add_xaxis(us_x_data)

# 给折线图添加y轴对象
line.add_yaxis('美国确诊', us_y_data, label_opts=LabelOpts(False))  # 添加美国确诊人数
line.add_yaxis('美国治愈', us_y_data_zy, label_opts=LabelOpts(False))  # 添加美国治愈人数
line.add_yaxis('美国死亡', us_y_data_sw, label_opts=LabelOpts(False))  # 添加美国死亡人数
line.add_yaxis('美国新增确诊', us_y_data_xz, label_opts=LabelOpts(False))  # 添加美国新增确诊人数

line.add_yaxis('日本确诊', jp_y_data, label_opts=LabelOpts(False))  # 添加日本确诊人数
line.add_yaxis('日本治愈', jp_y_data_zy, label_opts=LabelOpts(False))  # 添加日本治愈人数
line.add_yaxis('日本死亡', jp_y_data_sw, label_opts=LabelOpts(False))  # 添加日本死亡人数
line.add_yaxis('日本新增确诊', jp_y_data_xz, label_opts=LabelOpts(False))  # 添加日本新增确诊人数

line.add_yaxis('印度确诊', india_y_data, label_opts=LabelOpts(False))  # 添加印度确诊人数
line.add_yaxis('印度治愈', india_y_data_zy, label_opts=LabelOpts(False))  # 添加印度治愈人数
line.add_yaxis('印度死亡', india_y_data_sw, label_opts=LabelOpts(False))  # 添加印度死亡人数
line.add_yaxis('印度新增确诊', india_y_data_xz, label_opts=LabelOpts(False))  # 添加印度新增确诊人数

# 设置全局配置项
line.set_global_opts(
	title_opts=TitleOpts(title="2020年疫情情况", pos_left='center', pos_bottom='1%'),
	toolbox_opts=ToolboxOpts(is_show=True, pos_left='center', pos_bottom='50%'),
	legend_opts=LegendOpts(is_show=True),
	visualmap_opts=VisualMapOpts(is_show=True, pos_bottom='13%')
)

# 通过render()将代码转化为图像
line.render()


# 关闭打开的文件
f_us.close()
f_india.close()
f_jp.close()