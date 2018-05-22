'''
	Describtion: 航天飞行器是一项复杂而又精密的仪器，飞行器的损耗主要集中在发射和降落的过程，科学家根据
实验数据估计，如果在发射过程中，产生了 x 程度的损耗，那么在降落的过程中就会产生 x2 程度的损耗，如果飞船
的总损耗超过了它的耐久度，飞行器就会爆炸坠毁。问一艘耐久度为 h 的飞行器，假设在飞行过程中不产生损耗，那
么为了保证其可以安全的到达目的地，只考虑整数解，至多发射过程中可以承受多少程度的损耗？

	Analysis: 就是解二元一次不等式x^2 + x <= h。
'''

import math

h = int(input())
n1 = int(math.sqrt(h))
n2 = n1 + 1
if n1 * n2 > h:
    print(n1-1)
elif n1 * n2 == h:
    print(n1)
else:
    print(n2-1)