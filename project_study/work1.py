class Student:
	def __init__(self, name, age, address):
		self.name = name,
		self.age = age,
		self.address = address


stus = []
for x in range(2):
	print(f'录入第{x + 1}名学生的信息')
	name = input('输入你的名字:')
	age = input('输入你的年龄:')
	address = input('输入你的地址:')
	stu = Student(name, age, address)
	stus.append(stu)

for i in stus:
	print('学生信息:')
	print(f'姓名:{i.name},年龄:{i.age}, 地址:{i.address}')