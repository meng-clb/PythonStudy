# # 导包
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts,ToolboxOpts,LegendOpts,VisualMapOpts
#
# # 创建一个折线图对象
# line = Line()
#
# # 给折线图添加x轴对象
# line.add_xaxis(["中国", "日本", "美国"])
#
# # 给折线图添加y轴对象
# line.add_yaxis("GPD", [30, 10, 40])
#
# # 设置全局配置项
# line.set_global_opts(
# 	title_opts=TitleOpts(title="GDP展示", pos_left='center', pos_bottom='1%'),
# 	toolbox_opts=ToolboxOpts(is_show=True),
# 	legend_opts=LegendOpts(is_show=True),
# 	visualmap_opts=VisualMapOpts(is_show=True, pos_bottom='13%')
# )
#
# # 通过render()将代码转化为图像
# line.render()
