#jiecheng.py
def fact(n):
    if n ==0:
        return 1
    else:
        return n * fact(n-1)
n = eval(input("请输入阶乘数字："))    
print("{}阶乘的结果是{}".format(n,fact(n)))
