# 将接收到的函数进行反转返回
def str_reverse(s):
	s_len = len(s)
	str = []
	s_r = ""
	for x in s:
		str.append(x)

	for x in str:
		s_r += str[s_len - 1]
		s_len -= 1

	return s_r

# 对照传入的参数,对字符串进行切片
def substr(s,x,y):
	str = s[x:y]
	# print(str)
	return str
# substr('abcdefg', 2,5)