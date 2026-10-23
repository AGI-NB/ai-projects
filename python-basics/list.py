# num_list = []

# for i in range(1,21):
#     num = int(input('请输入一个有效数字：'))
#     num_list.append(num)

# num_list.sort()
# print('排列后的数字列表；',num_list)
# print('最大值：',num_list[-1])
# print('最小值：',num_list[0])
# print('平均值:',sum(num_list)/len(num_list))  #sum()求和；len()获取元素的个数(列表的长度)

# 1. 定义与合并
num_list1 = [19,23,12,34,54,213,12,323,23,52,6,67,7,4]
num_list2 = [234,45,54,87,98,7,3,8,4,68,874,78,67,7]
merged_list = num_list1 + num_list2  # merged_list = [*num_list1,*num_list2] 解包：将列表溶解为单个元素
print('合并后的列表：', merged_list)

# 2. 高效去重
unique_list = list(set(merged_list))
print('去重后的列表：', unique_list)

# 3. 列表推导式
square_list = [i**2 for i in range(1, 21)]
print('1-20的平方：', square_list)

even_square_list = [i**2 for i in range(1, 21) if i % 2 == 0]
print('1-20中偶数的平方：', even_square_list)