#text
import time
scale = 10
print("--------执行开始---------")
for i in range(scale+1):
    a = '*' * i
    b = '-' * (scale - i)
    c = i / scale * 100%
    sleep(1)
    print("{:.%}:{a}{b}".format(c,a,b))
print("--------执行结束---------")
