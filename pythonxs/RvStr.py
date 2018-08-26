#RvStr.py
def rvs(s):
    if s == "":
        return s
    else :
        return rvs(s[1:])+s[0]
n = input("请输入需要反转的字符串：")
print("反转之后的字符串为：{}".format(rvs(n)))
