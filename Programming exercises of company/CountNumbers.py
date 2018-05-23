'''
	Describtion: “回文串”是一个正读和反读都一样的字符串，比如“level”或者“noon”等等就是回文串。花花非常
喜欢这种拥有对称美的回文串，生日的时候她得到两个礼物分别是字符串A和字符串B。现在她非常好奇有没有办法将
字符串B插入字符串A使产生的字符串是一个回文串。你接受花花的请求，帮助她寻找有多少种插入办法可以使新串是
一个回文串。如果字符串B插入的位置不同就考虑为不一样的办法。

	Analysis: 切片的应用。
'''

s1 = input()
s2 = input()

count = 0
for i in range(len(s1)+1):
    s3 = s1[:i] + s2 + s1[i:]
    if len(s3)%2 == 0 :
        tmp = s3[len(s3)//2:]
        if s3[:len(s3)//2] == tmp[::-1]:
            count = count + 1
    elif len(s3)%2 == 1 :
        tmp = s3[(len(s3)+1)//2:]
        if s3[:len(s3)//2] == tmp[::-1]:
            count = count + 1

print(count)