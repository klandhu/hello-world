#TextProBarV3.py
import time
scale = 50
start = time.perf_counter()
print("执行的开始".center(scale//2,"-"))
for i in range(scale + 1):
      a = '*' * i
      b = '-' * (scale - i)
      c = (i / scale) * 100
      dur = time.perf_counter() - start
      print("\r{:3.0f}%[{}->{}]{:.2f}".format(c,a,b,dur),end = "")
      time.sleep(0.1)
print("\n"+"执行的结束".center(scale//2,"-"))
#print默认值被改变，必须重新设置。
#标点符号及变量拼写还存在问题，，马虎必须改掉，，注意力集中
