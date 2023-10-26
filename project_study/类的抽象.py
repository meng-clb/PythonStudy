"""
类的抽象
定义出一个抽象类, 只确定方法, 不实现方法, 用于对子类的约束
定义的子类复写抽象类的方法,
"""


class AC:
	def cool_wind(self):
		"""制冷"""
		pass

	def hot_wind(self):
		"""制热 """
		pass

	def swing_l_r(self):
		"""左右摆风"""
		pass


# 从父类继承, 复写父类的方法
class Midea_AC(AC):
	def cool_wind(self):
		print('美的空调独家制冷')

	def hot_wind(self):
		print('美的空调独家制热')

	def swing_l_r(self):
		print('美的空调左右摆风')


class Gree_AC(AC):
	def cool_wind(self):
		print('格力空调独家制冷')

	def hot_wind(self):
		print('格力空调独家制热')

	def swing_l_r(self):
		print('格力空调左右摆风')


def make_cool(ac: AC):
	ac.cool_wind()


# 对子类进行创建对象
midea_ac = Midea_AC()
gree_ac = Gree_AC()

# 传入调用的子类
make_cool(midea_ac)
make_cool(gree_ac)
