#CalPiV2.py
from random import random
from time import perf_counter
DARTS = 1000*1000     #可以控制撒点总数，得到更为精确的数字
hits = 0              #0.0和0都可以，本身就是计算单位，但是防止出现取整计算导致
start = perf_counter()
for i in range(1,DARTS+1):
    x,y = random(),random()
    dist =pow(x**2 + y**2,0.5)
    if dist <= 1:
        hits  = hits + 1
pi = 4 * (hits/DARTS)
print("圆周率的值是：{:.5f}".format(pi))
print("运行的时间是：{}".format(perf_counter()-start))


