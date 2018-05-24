'''
	Describtion: 考拉有n个字符串字符串，任意两个字符串长度都是不同的。考拉最近学习到有两种字符串的排序方法： 
1.根据字符串的字典序排序。例如："car" < "carriage" < "cats" < "doggies < "koala"
2.根据字符串的长度排序。例如："car" < "cats" < "koala" < "doggies" < "carriage"
考拉想知道自己的这些字符串排列顺序是否满足这两种排序方法，考拉要忙着吃树叶，所以需要你来帮忙验证。

	Analysis: 很常规的题，写两个比较函数即可。
'''

import sys

def reader():
    for i in sys.stdin:
        yield i.strip()

def dir_compare(s):
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return 0
        else:
            continue
    return 1

def len_compare(s):
    for i in range(len(s)-1):
        if len(s[i]) > len(s[i+1]):
            return 0
        else:
            continue
    return 1

n = int(input())
read = reader()
data = []
for i in range(n):
    data.append(next(read))
if dir_compare(data) == 1 and len_compare(data) == 1:
    print('both')
elif dir_compare(data) == 1 and len_compare(data) == 0:
    print('lexicographically')
elif dir_compare(data) == 0 and len_compare(data) == 1:
    print('lengths')
else:
    print('none')