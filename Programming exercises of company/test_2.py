'''
	Description: 一个由小写字母组成的字符串可以看成一些同一字母的最大碎片组成的。
例如,"aaabbaaac"是由下面碎片组成的:'aaa','bb','c'。牛牛现在给定一个字符串,请你帮助计算这个字符串
的所有碎片的平均长度是多少（结果四舍五入保留两位小数）。

	Analysis: 主要注意要求四舍五入且保留两位小数，除了使用round函数外，还得限制小数位数，例如：3.50
'''

list = list(input())
count = 1
p = []
for i in range(1,len(list)):
    if list[i] == list[i-1]:
        count = count + 1
    else:
        p.append(count)
        count = 1
p.append(count)
print('%.2f'%round(sum(p)/len(p), 2))