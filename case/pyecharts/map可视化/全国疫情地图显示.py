"""
全国疫情地图显示
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 处理数据
f = open("./疫情.txt", "r", encoding="UTF-8")
f_data = f.read()
f.close()
data = json.loads(f_data)
data_areaTree = data['areaTree'][0]['children']

# 把拿到的数据处理为地图可用的元组
data_list = []
for data in data_areaTree:
	if data['name'] == '上海' or data['name'] == '北京' or data['name'] == '天津' \
			or data['name'] == '重庆':
		data_name = data['name'] + '市'
	elif data['name'] == '香港' or data['name'] == '澳门':
		data_name = data['name'] + '特别行政区'
	elif data['name'] == '西藏' or data['name'] == '内蒙古':
		data_name = data['name'] + '自治区'
	elif data['name'] == '新疆':
		data_name = data['name'] + '维吾尔自治区'
	elif data['name'] == '宁夏':
		data_name = data['name'] + '回族自治区'
	elif data['name'] == '广西':
		data_name = data['name'] + '壮族自治区'
	else:
		data_name = data['name'] + '省'
	data_list.append((data_name, data['total']['confirm']))

ff = open('test.txt', 'w', encoding="UTF-8")
ff.write(str(data_list))


# 创建地图对象
map = Map()

map.add("全国疫情确诊", data_list, "china")
# 设置全局变量
map.set_global_opts(
	visualmap_opts=VisualMapOpts(
		is_show=True,
		is_piecewise=True,
		pieces=[
			{"min": 1, "max": 9, "label": "1-9人", "color": "#FFE4C4"},
			{"min": 10, "max": 999, "label": "10-9999人", "color": "#FF6A6A"},
			{"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#EEE685"},
			{"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#B8860B"},
			{"min": 100000, "label": "100000+人", "color": "#8B4513"},
		]
	)
)

# 图像映射
map.render("全国疫情确诊情况.html")
