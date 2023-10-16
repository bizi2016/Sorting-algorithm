# radix_sort 代码实现

from typing import List

def radix_sort(nums: List[int]):
    
    n = len(str(max(nums)))  # 记录最大值的位数
    
    for k in range(n):  # n轮排序
        # 每一轮生成10个列表
        bucket_list = [ [] for i in range(10) ]  # 因为每一位数字都是0~9，故建立10个桶
        for i in nums:
            # 按第k位放入到桶中
            bucket_list[ i // (10**k) % 10 ].append(i)
        # 按当前桶的顺序重排列表
        nums = [ j for i in bucket_list for j in i ]
        print(k, nums)
        
    return nums



if __name__ == '__main__':
    
    nums = [ 3321, 5613, 7343, 2645, 3214, 5629, 7171, 9201, 3886, 2437 ]
    print(nums)
    print()
    
    nums = radix_sort(nums)
