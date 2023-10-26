class Student:
	# 私有变量,外部不可访问
	__score = None

	# 内置初始化函数,当对象创建时,这个函数自动启用
	def __init__(self, name, age, sex, native_place, score):
		self.name = name
		self.age = age
		self.sex = sex
		self.native_place = native_place
		self.__score = score

	# 私有变量,外部不可访问
	def __Score(self):
		print(self.__score)

	# 私有变量,可以被内部方法使用
	def show_score(self):
		if self.__score >= 90:
			self.__Score()
		else:
			print('成绩不对外显示')


stu1 = Student('clb', 14, 'man', 'china', 99)
print(stu1.name)
try:
	stu1.__Score()
	print(stu1.__score)
except:
	print('__x是私有变量,对象不可直接调用')

stu1.show_score()
