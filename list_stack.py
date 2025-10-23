'''
列表与栈
nums.append('添加数的大小') 默认加到末尾
nums.pop()删除最后一个,括号无内容，函数默认等于最后一个数
stack后进先出（LIFO）
'''
def remove_dulplicates(nums):
    '''
    功能：删除列表中的重复元素，保持原有顺序
    :param nums: 输入列表
    :return: 去重后的新列表
    '''
    stack=[]
    for num in nums:
        if num not in stack:
            stack.append(num)
    return stack

#nums=[2,2,2,11,11,4,5,1,2]
#print(remove_dulplicates(nums))
#创建一个存储列表记录新的数字，用not作逻辑判断

def serchinsert1(nums,target):
    '''
    寻找位置或插入位置
    :param nums: 有序列表
    :return: 位置

    for i,num in enumerate(nums):
        if num>=target:
            return i
        else:
            return len(nums)
        #else应该放在循环外，否则每次都会执行else

        一旦执行到 return 语句，函数会立即结束，
        后面的代码（包括别的 return）不会再执行。
    '''
    for i, num in enumerate(nums):
        if num >= target:
            return i
    return len(nums)

def searchinsert2(nums,target):
    '''
    二分法查找 binary search
    需要满足数据有序且可索引
    :param nums: 数组
    :param target: 目标
    :return: 位置
    '''
    left=0
    right=len(nums)-1

    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return left





#nums=[1,3,4,54,64]
#target=56
#print(searchinsert2(nums,target))
#注意，在对列表进行索引时，需要[],而不是()
