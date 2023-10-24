"""
print_file_info(file_name)
接收传入文件的路径,打印文件的全部内容,如果文件不存在则铺货异常,
输出提示信息,通过finally关闭文件对象
"""


def print_file_info(file_name):
	"""
	打印文件内的内容
	:param file_name: 文件路径
	"""
	try:
		f = open(file_name, "r", encoding="UTF-8")
		print(f.read())
	except:
		print(f'文件出现了错误')
	finally:
		try:
			f.close()
		except:
			print('文件未打开')


# print_file_info('../test.txt')

"""
append_to_file(file_name, data)
接收文件路径以及传入数据,将数据追加写入到文件中
"""


def append_to_file(file_name, data):
	"""
	将传入的数据写入到文件内
	:param file_name: 文件路径
	:param data: 写入的数据
	"""
	try:
		file = open(file_name, "a", encoding="UTF-8")
		file.write('\n' + data)
	except FileNotFoundError:
		print('未找到文件,请检查文件路径')
	finally:
		try:
			file.close()
		except:
			pass


