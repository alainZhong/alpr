s=input('请输入一段字符串:')

letters=0
digits=0
spaces=0

for ch in s:
    if ch.isdigit():
        digits+=1
    if ch.isalpha():
        letters+=1
    if ch.isspace():
        spaces+=1
print(f'字母有{letters},数字有{digits}，空格有{spaces}')

#多种计数需要提前初始化计数器，并且有内置的判断函数，与for循环配合计数
#ch 作为character的缩写，数字的英文是digit