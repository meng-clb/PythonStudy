# 导包
from pyecharts.charts import Line

# 创建一个折线图对象
line = Line()

# 给折线图添加x轴对象
line.add_xaxis(["中国", "日本", "美国"])

# 给折线图添加y轴对象
line.add_yaxis("GPD", [30, 10, 40])

# 通过render()将代码转化为图像
line.render()

# 设置全局配置项
