def bucket_sort(nums):

    min_data, max_data = min(nums), max(nums)

    bucket_size = (max_data - min_data) / len(nums)

    buckets = [ [] for i in range(len(nums)+1) ]

    for i in nums:
        index = int( (i - min_data) / bucket_size )
        buckets[index].append(i)

    # print(buckets)

    nums.clear()
    for i in buckets:
        nums.extend(sorted(i))



if __name__ == '__main__':

    n = 20
    nums, test = list(range(n)), list(range(n))

    import random
    
    for i in range(100000):
        
        random.shuffle(nums)
        bucket_sort(nums)
        
        if nums != test:
            print(nums)
