#fibV1.py
def fib(n):
    if n ==1 or n == 2:
        print(1)
        
    else:
        s=fib(n-1) + fib(n-2)
        print(s)
n = eval(input("斐波那契数列计算："))
print("斐波那契数列为：{}".format(fib(n)))
        
'''def f(n):
    if(n<=2):
        return 1
    else:
        return f(n-1)+f(n-2)

if __name__=="__main__":
    num=int(input("请输入你要输出的斐波那契数列的项数："))
    if num<0:
        print("请输入一个正整数")
    else:
        print("斐波那契数列的前{}项为：".format(num))
        for i in range(1,num+1):
            print(f(i),end=" ")
'''
