'''
	Describtion: 小易喜欢的单词具有以下特性：1.单词每个字母都是大写字母;2.单词没有连续相等的字母;
3.单词没有形如“xyxy”(这里的x，y指的都是字母，并且可以相同)这样的子序列，子序列可能不连续。例如：
	小易不喜欢"ABBA"，因为这里有两个连续的'B'
	小易不喜欢"THETXH"，因为这里包含子序列"THTH"
	小易不喜欢"ABACADA"，因为这里包含子序列"AAAA"
	小易喜欢"A","ABA"和"ABCBA"这些单词
	给你一个单词，你要回答小易是否会喜欢这个单词。

	Analysis: 大小写的判断可以使用正则表达式。对不连续子串的判断，利用循环找出同一字符出现的位置i和j，
再嵌套一层循环比较i和j之间的子串与j之后的子串中是否有相同的字符。
'''

import re
s = list(input().strip())

def compare1(s):
    for i in s:
        if re.match(r'a~z',i):
            return 0
        else:
            continue
    return 1

def compare2(s):
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
        	# 如果j-i=1，则表示有两个连续的相同字符
            if s[i] == s[j] and j - i == 1:
                return 0
            elif s[i] == s[j] and j - i != 1:
            	# 比较i和j之间的子串与j之后的子串中是否有相同的字符
                for m in range(i+1,j):
                    for n in range(j+1,len(s)):
                        if s[m] == s[n]:
                            return 0
            else:
                continue
    return 1

if compare1(s) and compare2(s):
    print('Likes')
else:
    print('Dislikes')