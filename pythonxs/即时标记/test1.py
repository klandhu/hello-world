import sys
def lines(file):
    for line in open(file):
        yield line
    yield '\n'


f=next(lines(r'D:\PycharmProjects\asigntime\test_input.txt'))
for i in lines(r'D:\PycharmProjects\asigntime\test_input.txt'):
    print(i)
#x=lines(r'D:\PycharmProjects\asigntime\test_input.txt')
#print(x)
'''
f = open(r'D:\PycharmProjects\asigntime\test_input.txt')  
while True:  
    line = f.readline()  
    if not line: break  
    print(line)  
f.close()
'''
