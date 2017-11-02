'''
	Description: 小易有一个长度为n的整数序列,a_1,...,a_n。然后考虑在一个空序列b上进行n次以下操作:
		1、将a_i放入b序列的末尾
		2、逆置b序列
	小易需要你计算输出操作n次之后的b序列
	
	Analysis: list的切片应用
'''

n = int(input())
data = list(input().split())
b= []
if n%2 == 0:
    b[:int(n/2)] = data[::-2]
    b[int(n/2):] = data[::2]
else:
    b[:int((n+1)/2)] = data[::-2]
    b[int((n+1)/2):] = data[1::2]
 
print(' '.join(b))