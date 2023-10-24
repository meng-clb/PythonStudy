import mymodel as model
import platform

model.print_myname('clb')

model.pr_information(model.person1['age'])

model_list = dir(model)
for x in model_list:
	print(x)

platform_list = dir(platform)
for x in platform_list:
	print(x)