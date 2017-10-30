'''
	Description: 小易有一个长度为N的正整数数列A = {A[1], A[2], A[3]..., A[N]}。牛博士给小易出了一个难题:
对数列A进行重新排列,使数列A满足所有的A[i] * A[i + 1](1 ≤ i ≤ N - 1)都是4的倍数。小易现在需要判断一个
数列是否可以重排之后满足牛博士的要求。

	Analysis: 很明显，如果奇数的个数大于4的倍数的数的个数，则不能实现上述要求。
'''

import sys
 
def read():
    for line in sys.stdin:
        yield list(map(int, line.split()))
 
n = int(input())
r = read()
for i in range(n):
    length = next(r)[0]
    l = next(r)
    p1 = []
    p2 = []
    p4 = []
    for i in l:
        if i%4 == 0:
            p4.append(i)
        elif i%2 == 0:
            p2.append(i)
        else:
            p1.append(i)
             
    if len(p1) > len(p4):
        print('No')
    else:
        print('Yes')