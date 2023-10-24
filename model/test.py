import mymodel as model     # 引入自定义模块
import platform  # 系统内置模块
from time import sleep  # 引用time模块中的sleep功能函数

# 使用导入的功能
print('5s后输出执行后边的一系列操作')
sleep(5)
print('5s end')

# 使用自定义模块内的功能
model.print_myname('clb')
model.pr_information(model.person1['age'])

# 使用dir函数打印所有的模块内功能
# 自定义模块的功能
model_list = dir(model)
for x in model_list:
	print(x)

# 系统内置的模块
platform_list = dir(platform)
for x in platform_list:
	print(x)
