f = open("clb.txt", "w")
f.close()
try:
	f = open("clb.txt","w")
	f.write("这是一个测试文本")
except: # try不能运行时,运行此语句
	print("此文件不可写入")
finally: # 无论上边是否执行,都会执行
	f.close()

clb_f = open("clb.txt", "r")
print(clb_f.read())
clb_f.close()