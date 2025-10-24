#.count()
#统计某个子元素或字符串出现的次数
#计算从1到2020，共出现过多少次2
count=0
for i in range(1,2021):
    count+=str(i).count('2')
print(count)