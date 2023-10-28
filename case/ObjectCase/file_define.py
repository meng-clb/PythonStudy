import json

from data_define import Record


# 定义一个抽象类
class FileReader:
	def read_data(self) -> list[Record]:
		# 读取文件的数据,读取的每一行数据都转换为Record对象,将它们都封装到list内返回即可
		pass


# 定义子类, 读取txt文本中的数据
class TextFileReader(FileReader):
	def __init__(self, path):
		self.path = path

	# 复写父类的方法
	def read_data(self) -> list[Record]:
		record_list: list[Record] = []
		f = open(self.path, "r", encoding="UTF-8")
		for line in f.readlines():
			line = line.strip()
			data_list = line.split(",")
			record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
			record_list.append(record)

		f.close()
		return record_list


class JsonFileReader(FileReader):
	def __init__(self, path):
		self.path = path

	# 复写父类的方法
	def read_data(self) -> list[Record]:
		record_list: list[Record] = []
		f = open(self.path, "r", encoding="UTF-8")
		for line in f.readlines():
			line = line.strip()
			f_dict = json.loads(line)
			record = Record(f_dict['date'], f_dict['order_id'], int(f_dict['money']), f_dict['province'])
			record_list.append(record)

		f.close()
		return record_list


if __name__ == '__main__':
	test_file_reader = TextFileReader("one.txt")
	json_file_reader = JsonFileReader("two.txt")
	list1 = test_file_reader.read_data()
	list2 = json_file_reader.read_data()

	for l in list1:
		print(l)

	for l in list2:
		print(l)

