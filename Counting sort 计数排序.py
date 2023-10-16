def counting_sort(nums):
    
    if len(nums) <= 1:
        return nums
    
    max_num = max(nums)
    counter = [0] * (max_num + 1)
    
    for num in nums:
        counter[num] += 1

    nums.clear()
    nums = [ i for i in range(len(counter)) for j in range(counter[i]) ]
    
    return nums
 

 
if __name__ == '__main__':
    
    nums = [5, 7, 3, 7, 2, 3, 2, 5, 9, 5, 7, 6]
    print(counting_sort(nums))
    # [2, 2, 3, 3, 5, 5, 5, 6, 7, 7, 7, 9]
