def str_reverse(s):
	"""
	将接收到的函数进行反转返回
	:param s: 接收到的字符串
	:return: 返回字符串的反转值
	"""
	s_len = len(s)
	str = []
	s_r = ""
	for x in s:
		str.append(x)

	for x in str:
		s_r += str[s_len - 1]
		s_len -= 1

	return s_r


def substr(s,x,y):
	"""
	对传入的字符串进行切片
	:param s: 传入的字符串
	:param x: 开始切片的位置
	:param y: 结束切片的位置
	:return: 切片的数据
	"""
	str = s[x:y]
	# print(str)
	return str
# substr('abcdefg', 2,5)