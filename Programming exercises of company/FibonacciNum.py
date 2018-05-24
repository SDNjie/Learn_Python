'''
	Describtion: Fibonacci数列是这样定义的：F[0] = 0, F[1] = 1,for each i ≥ 2: F[i] = F[i-1] + F[i-2]
因此，Fibonacci数列就形如：0, 1, 1, 2, 3, 5, 8, 13, ...，在Fibonacci数列中的数我们称为Fibonacci数。给
你一个N，你想让其变为一个Fibonacci数，每一步你可以把当前数字X变为X-1或者X+1，现在给你一个数N求最少需要
多少步可以变为Fibonacci数。

	Analysis: 找出输入的数字在哪两个Fibonacci数字之间即可。
'''

n = int(input())
a, b = 0, 1
if n == 0 or n == 1:
    print(0)
else:
    flag = abs(n - b)
    while True:
        a, b = b, a+b
        if flag == 0:
            print(0)
            break
        else:
            if abs(n - b) <= flag:
                flag = abs(n - b)
            else:
                print(flag)
                break