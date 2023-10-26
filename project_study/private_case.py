class Phone:

	def __is_5g_enable(self):
		"""
		私有成员变量,类型bool, True开启5g,False关闭
		:return:
		"""
		return False

	def __check_5g(self):
		if self.__is_5g_enable():
			print('5g开启')
		else:
			print('5g关闭,使用4g网络')

	def call_by_5g(self):
		self.__check_5g()


phone = Phone()
phone.call_by_5g()