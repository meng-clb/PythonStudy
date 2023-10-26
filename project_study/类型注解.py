# 类型注解, 调用方法时,可以有代码提示类型
def add(x: int, y: int) -> int:
	return x + y


print(add(3, 4))


def func(data: list):
	pass


func([3, 5, 1])

"""
Union类型注解
使用Union类型注解需要先导包
"""
from typing import Union

my_list: list[Union[int, str]] = [1, 4, 'str']


def fun(data: Union[int, str]) -> [Union[int, str]]:
	pass


fun(3)
fun('clb')
