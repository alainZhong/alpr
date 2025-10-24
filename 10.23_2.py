#print(365*20+20/4+1-62-30+1)7215
#print(12*19+10)238
#print(7215//7)1030+1
#print(7215+238+1031)8484

'''
datetime库
date,timedelta函数
产生一个日期数据
.day调用day
.weekday()返回一个星期数，前者是属性，后者是函数，调用函数需要（）
核心是运用while和or判断语句

from datetime import date,timedelta

start=date(2000,1,1)
end=date(2020,10,1)

total=0
current=start

while current<=end:
    if current.day==1 or current.weekday()==0:
        total+=2
    else:
        total+=1
    current+=timedelta(days=1)
print(total)
'''

from datetime import date,timedelta

start=date(2000,1,1)
end=date(2020,10,1)

current=start
total=0

while current<=end:
    if current.day==1 or current.weekday()==0:
        total+=2
    else:
        total+=1
    current+=timedelta(1)
print(total)




