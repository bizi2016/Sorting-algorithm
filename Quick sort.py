import random



def partition(nums, low, high):
    """
    将数组nums在区间[low, high]中进行分区操作，选择最右边的元素作为pivot，
    将小于等于pivot的元素放在pivot的左边，大于pivot的元素放在pivot的右边，
    并返回pivot的索引位置。
    
    Args:
        nums (list): 待分区的数组。
        low (int): 分区的起始索引。
        high (int): 分区的结束索引。
        
    Returns:
        int: pivot的索引位置。
    """
    # 随机挑选基准值
    pick = random.randint(low, high)
    nums[pick], nums[high] = nums[high], nums[pick]
    
    i = low - 1  # 初始化最小元素索引
    
    pivot = nums[high]  # 选择最右边的元素作为 pivot

    # 0-i 是已经处理过的区间（小于基准）
    # i-j 是已经处理过的区间（大于基准）
    # j 是正在处理的那个元素
    for j in range(low, high):
        # 当前元素小于或等于 pivot，将其交换到已处理区间的末尾
        if nums[j] <= pivot:
            i = i + 1
            # 将当前元素与已处理区间的下一个元素交换
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
            # else: print('S', end='')

    i += 1
    # 将 pivot 放到正确的位置上，即已处理区间的末尾
    nums[i], nums[high] = nums[high], nums[i]
    return i  # 返回 pivot 的索引位置



# nums[]    --> 待排序的数组
# low       --> 子数组的起始索引
# high      --> 子数组的结束索引

# 快速排序函数
def quickSort(nums, low, high):
    """
    使用快速排序算法对数组nums在区间[low, high]中进行排序。
    
    Args:
        nums (list): 待排序的数组。
        low (int): 子数组的起始索引。
        high (int): 子数组的结束索引。
        
    Returns:
        None: 原数组被就地排序，不需要返回新数组。
    """
    if low < high:
        # 对当前子数组进行分区操作，获取 pivot 的索引位置
        pivot = partition(nums, low, high)
        
        # 递归地对 pivot 左边的子数组进行快速排序
        quickSort(nums, low, pivot - 1)
        
        # 递归地对 pivot 右边的子数组进行快速排序
        quickSort(nums, pivot + 1, high)



if __name__ == '__main__':
    # 当模块直接运行时执行以下代码

    nums = list(range(20))  # 创建一个包含 0 到 19 的整数列表
    random.shuffle(nums)  # 将列表中的元素随机打乱
    print(nums)

    quickSort(nums, 0, len(nums) - 1)  # 使用快速排序算法对列表进行排序
    print(nums)  # 打印排序后的列表










