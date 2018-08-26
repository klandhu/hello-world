#AutoTraceDraw.py
import turtle as t
t.title('自动轨迹绘制')
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)
#数据读取
datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n","")
    datals.append(list(map(eval,line.split(","))))
f.close()
#自动绘制
for i in range(len(datals)):
<<<<<<< HEAD
    t.pencolor(datals[i][3],datals[i][4],data[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.rt(datals[i][2])
    else:
        t.lt(datals[i][2])
=======
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
>>>>>>> f4cb1ea8b6fda3e22eab3e76c6d75de93eca18a9
