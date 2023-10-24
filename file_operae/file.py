# 源文件读取
f_test = open("test.txt", "r")

# 拷贝test.txt.bak
f_test_bak = open("test.txt.bak", "w")


count = 0
# 符合条件的拷贝出来
for x in f_test:
	x = x.replace("\r", "")
	if "0" in x or "1" in x or "2" in x or "3" in x or "4" in x or "5" in x or "6" in x or "7" in x or "8" in x or "9" in x:
		continue
	elif x == "\n":
		continue
	else:
		if count == 50 :
			count = 0
			f_test_bak.write("\n")
		else:
			count += 1
			f_test_bak.write(x)

# 读取拷贝的文件
f_test_bak = open("test.txt.bak", "rt")
print(f_test_bak.read())
# 关闭文件
f_test.close()
f_test_bak.close()
