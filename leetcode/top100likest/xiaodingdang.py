# -*- coding:utf-8 -*-
'''
author:zhangyu
date:2020/2/25
'''

#画叮当猫。
import turtle;
t=turtle.Pen()
#画头
t.fillcolor("blue")
t.begin_fill()
t.circle(160)
t.end_fill()
#画脸
t.fillcolor("white")
t.begin_fill()
t.circle(130)
t.end_fill()
#画眼睛
t.up()
t.goto(-20,240)#第一只眼睛（左）
t.down()
t.fillcolor("#fff")
t.begin_fill()
t.circle(20)
t.up()
t.goto(20,240)#第二只眼睛
t.down()
t.circle(20)
t.end_fill()

#画里面的眼珠黑色部分
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.up()
t.goto(-20,240)
t.down()
t.circle(10)
t.end_fill()

#画鼻子
t.up()
t.goto(0,200)
t.down()
t.fillcolor("red")
t.begin_fill()
t.circle(20)
t.end_fill()
t.right(90)
t.forward(70)
#画嘴巴
t.up()
t.goto(-50,100)
t.down()
t.circle(50,180)

#画胡子
t.up()
t.goto(20,150)
t.down()
t.right(100)
t.forward(80)
t.up()
t.goto(20,180)
t.down()
t.left(30)
t.forward(80)

t.up()
t.goto(20,160)
t.down()
t.left(-10)
t.forward(80)

#画左边胡子
t.up()
t.goto(-20,160)
t.down()
t.right(180)
t.forward(80)

t.up()
t.goto(-20,180)
t.down()
t.right(20)
t.forward(80)

t.up()
t.goto(-20,150)
t.down()
t.right(-40)
t.forward(80)

t.up()
t.goto(0,-50)
t.write("Author：zhangyu", align="left",font=("微软雅黑", 16, "bold"))

turtle.done()


