"""
可视化地图的基本使用
"""

# 导包
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 创建基础对象
map = Map()

# 准备数据
data = [
	("上海市", 99),
	("河南省", 4),
	("台湾省", 400),
	("香港特别行政区", 200)
]

# 添加数据
map.add("地图测试", data, maptype="china")

# 设置全局变量
map.set_global_opts(
	visualmap_opts=VisualMapOpts(
		is_show=True,
		is_piecewise=True,
		pieces=[
			{"min": 1, "max": 9, "label": "1-9人", "color": "#ccffff"},
			{"min": 10, "max": 99, "label": "10-99人", "color": "#ffff99"},
			{"min": 100, "max": 499, "label": "100-499人", "color": "#ff6666"},
		]
	)
)

# 生成地图
map.render("map.html")
