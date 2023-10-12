import random



def quickSort(nums):
        
    n = len(nums)

    # Recursive boundary conditions
    if n == 0 or n == 1:
        return nums

    # Quick sort python
    pivot = random.choice(nums)
    left, mid, right = [], [], []

    for i in nums:
        if i < pivot: left.append(i)
        elif i > pivot: right.append(i)
        else: mid.append(i)
        
    return quickSort(left) + mid + quickSort(right)



# Verify correctness
if __name__ == '__main__':

    nums, ans = list(range(20)), list(range(20))

    for i in range(100000):
        
        random.shuffle(nums)
        nums = quickSort(nums)
        
        if nums != ans:
            print(nums)
















