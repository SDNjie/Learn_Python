'''
	Describtion: 小易邀请你玩一个数字游戏，小易给你一系列的整数。你们俩使用这些整数玩游戏。
每次小易会任意说一个数字出来，然后你需要从这一系列数字中选取一部分出来让它们的和等于小易所说的数字。 
例如： 如果{2,1,2,7}是你有的一系列数，小易说的数字是11.你可以得到方案2+2+7 = 11.如果顽皮的小易想坑你，
他说的数字是6，那么你没有办法拼凑出和为6 现在小易给你n个数，让你找出无法从n个数中选取部分求和的数字中的最小数。

	Analysis: 首先，对list进行排序；其次，对于list的前i项和如果小于第i+1项减1，则不能求出的数的最小值即为前i项和加1。
'''

n = int(input())
l = list(map(int, input().split()))
l.sort()
m = []
t = 0
if l[0] == 1 and len(l) != 1:
    for i in range(1, n):
        if sum(l[0:i]) < l[i] - 1:
            t = sum(l[0:i])
            break
        if i == n-1 and sum(l[0:n-1]) >= l[n-1] - 1:
            t = sum(l[0:n])
    print(t+1)
elif l[0] == 1 and len(l) == 1:
    print(2)
else:
    print(1)