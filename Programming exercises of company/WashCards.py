'''
	Describtion: 洗牌在生活中十分常见，现在需要写一个程序模拟洗牌的过程。 现在需要洗2n张牌，从上到下
依次是第1张，第2张，第3张一直到第2n张。首先，我们把这2n张牌分成两堆，左手拿着第1张到第n张（上半堆），
右手拿着第n+1张到第2n张（下半堆）。接着就开始洗牌的过程，先放下右手的最后一张牌，再放下左手的最后一张牌，
接着放下右手的倒数第二张牌，再放下左手的倒数第二张牌，直到最后放下左手的第一张牌。接着把牌合并起来就可以了。 
例如有6张牌，最开始牌的序列是1,2,3,4,5,6。首先分成两组，左手拿着1,2,3；右手拿着4,5,6。在洗牌过程中按顺序放
下了6,3,5,2,4,1。把这六张牌再次合成一组牌之后，我们按照从上往下的顺序看这组牌，就变成了序列1,4,2,5,3,6。 
现在给出一个原始牌组，请输出这副牌洗牌k次之后从上往下的序列。

	Analysis: list的切片应用。
'''

import sys
def reader():
    for line in sys.stdin:
        for s in line.strip().split():
            yield s
read = reader()
T = int(next(read))
for t in range(T):
    n, k = int(next(read)), int(next(read))
    cards = []
    for i in range(2*n):
        cards.append(next(read))
    for j in range(k):
        tmp = cards[:]
        cards[::2] = tmp[:n]
        cards[1::2] = tmp[n:]
    print(' '.join(cards))