# 引入方式
# 直接引入包-模块
# import my_package.model1
# import my_package.model2
# my_package.model1.prModel()
# my_package.model2.prModel2()

# 通过from引入某个模块
# from my_package import model1
# model1.prModel()

# 通过from直接引入功能模块
# from my_package.model2 import prModel2
# prModel2()

# 通过 * 引入所有模块
from my_package import *
model1.prModel()

# 使用导入的功能
# print('5s后输出执行后边的一系列操作')
# sleep(5)
# print('5s end')

# 使用自定义模块内的功能
# model.print_myname('clb')
# model.pr_information(model.person1['age'])

# 使用dir函数打印所有的模块内功能
# 自定义模块的功能
# model_list = dir(model)
# for x in model_list:
# 	print(x)

# 系统内置的模块
# platform_list = dir(platform)
# for x in platform_list:
# 	print(x)
