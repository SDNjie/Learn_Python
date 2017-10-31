'''
	Description: 如果一个数列S满足对于所有的合法的i,都有S[i + 1] = S[i] + d, 这里的d也
可以是负数和零,我们就称数列S为等差数列。小易现在有一个长度为n的数列x,小易想把x变为一个
等差数列。小易允许在数列上做交换任意两个位置的数值的操作,并且交换操作允许交换多次。但是
有些数列通过交换还是不能变成等差数列,小易需要判别一个数列是否能通过交换操作变成等差数列。

	Analysis: 等差数列。对原始数列进行sort()方法排序，再进行判断即可。
'''

n = int(input())
data = list(map(int, input().split()))
data.sort()
index = data[1] - data[0]
flag = 0

for i in range(2, n):
    if data[i] - data[i-1] == index:
        continue
    else:
        flag = 1
        break
if flag == 0:
    print('Possible')
else:
    print('Impossible')