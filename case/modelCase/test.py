from my_utils import *  # 引入str_util文件 file_util
# s1 = str_util.str_reverse('I LOVE YOU')
# print(s1)
#
# s2 = str_util.substr('abcdefg', 1, 4)
# print(s2)

print('写入前读取')
file_util.print_file_info('./test.txt')
file_util.append_to_file('./test.txt', '这是我第2次追加内容')
print('写入后读取')
file_util.print_file_info('./test.txt')