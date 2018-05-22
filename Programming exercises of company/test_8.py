'''
	Description: 小易为了向他的父母表现他已经长大独立了,他决定搬出去自己居住一段时间。一个人
生活增加了许多花费: 小易每天必须吃一个水果并且需要每天支付x元的房屋租金。当前小易手中已经有f个
水果和d元钱,小易也能去商店购买一些水果,商店每个水果售卖p元。小易为了表现他独立生活的能力,希望
能独立生活的时间越长越好,小易希望你来帮他计算一下他最多能独立生活多少天。

	Analysis: 很简单，小学加减乘除的应用。但需要注意的是，刚开始所拥有的水果数量可能会超过将钱全部用于
租房的天数。
'''

data = list(map(int, input().split()))
if int(data[2]/data[0]) < data[1]:
    count = int(data[2]/data[0])
else:
    count = data[1] + int((data[2]-data[1]*data[0])/(data[0]+data[3]))
print(count)