'''
collecctions模块里三个函数：Count,deque,defaultdict

:Count(nums)
输入数组，输出一个字典，里面统计元素出现的次数

：deque
双边队列

：defaultdict
带默认值的词典

一、蓝桥杯班级活动：
给定一个长度为 n （偶数）的整数序列 a₁, a₂, … aₙ （每个 1 ≤ aᵢ ≤ n）。
你可以修改若干个数字，使得每个数字都出现恰好两次。
问最少需要修改多少个数。

1.
a = list(map(int,input().split()))
input接收一行数字
split拆成小的字符串
map将int映射到每个元素
list生成列表

'''
from collections import Counter
n=int(input())
nums=list(map(int,input().split()))

count=Counter(nums)
#Counter 作为一个类，应该作用在nums上，而不是nums的属性

sum_1=sum(1 for v in count.values() if v==1)
sum_e=sum(v-2 for v in count.values() if v>2)

if sum_1>=sum_e:
    result=sum_e+(sum_1-sum_e)//2
else:
    result=sum_e
print(result)

