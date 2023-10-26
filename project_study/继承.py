# 单继承
class Person:
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex

	def say_Hi(self):
		print(f'你好, 我是{self.name}')


class Student(Person):
	def identity(self):
		print('我是一个学生')


stu = Student('clb', 21, 'man')
stu.say_Hi()
stu.identity()


class Country:
	def my_country(self):
		print("China")


# 多继承
class People(Person, Country):
	pass


people = People('gg', 12, 'men')
people.my_country()
