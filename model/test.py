import mymodel as model
import platform
from time import sleep #引用time模块中的sleep功能函数

print('5s后输出执行后边的一系列操作')
sleep(5)
print('5s end')

model.print_myname('clb')

model.pr_information(model.person1['age'])

model_list = dir(model)
for x in model_list:
	print(x)

platform_list = dir(platform)
for x in platform_list:
	print(x)