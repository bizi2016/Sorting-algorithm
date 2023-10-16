import random



def bubble_sort(nums):
    
    n = len(nums)
    
    for i in range(n):
        swapped = 0
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = 1
        if swapped == 0: break



def insertion_sort(nums):

    n = len(nums)

    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key



def selection_sort(nums):

    n = len(nums)

    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j

        if i != min_index:
            nums[min_index], nums[i] = nums[i], nums[min_index]



def shell_sort(nums):

    n = len(nums)
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):
            key = nums[i]
            j = i - gap
            while j >= 0 and nums[j] > key:
                nums[j + gap] = nums[j]
                j -= gap
            nums[j + gap] = key

        gap //= 2



class HeapSort:

    def __init__(self, nums):
        self.nums = nums

    def heapify(self, n, root):

        largest = root
        left = root * 2 + 1
        right = root * 2 + 2

        if left < n and self.nums[largest] < self.nums[left]:
            largest = left
        if right < n and self.nums[largest] < self.nums[right]:
            largest = right
        if largest != root:
            self.nums[largest], self.nums[root] = self.nums[root], self.nums[largest]
            self.heapify(n, largest)

    def main(self):

        n = len(self.nums)

        for i in range(n, -1, -1):
            self.heapify(n, i)

        for i in range(n-1, 0, -1):
            self.nums[0], self.nums[i] = self.nums[i], self.nums[0]
            self.heapify(i, 0)



class QuickSort:

    def __init__(self, nums):
        self.nums = nums

    def partition(self, left, right):

        # Randomization
        pick = random.randint(left, right)
        self.nums[pick], self.nums[right] = self.nums[right], self.nums[pick]

        i = left - 1
        pivot = self.nums[right]

        for j in range(left, right):

            if self.nums[j] <= pivot:
                i += 1
                if i != j:
                    self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        i += 1
        self.nums[i], self.nums[right] = self.nums[right], self.nums[i]
        return i

    def main(self, left, right):

        if left < right:

            pivot = self.partition(left, right)

            self.main(left, pivot - 1)
            self.main(pivot + 1, right)



def quick_sort_python(nums):

    if len(nums) <= 1:
        return nums

    pivot = random.choice(nums)
    left, mid, right = [], [], []

    for i in nums:
        if i < pivot: left.append(i)
        elif i > pivot: right.append(i)
        else: mid.append(i)

    return quick_sort_python(left) + mid + quick_sort_python(right)



def divide(nums):

    n = len(nums)

    if n <= 1: return nums

    left, right = divide(nums[:n//2]), divide(nums[n//2:])

    return merge(left, right)



def merge(left, right):

    li, ri = 0, 0

    ans = []
    while li<len(left) and ri<len(right):
        if left[li] < right[ri]:
            ans.append(left[li])
            li += 1
        else:
            ans.append(right[ri])
            ri += 1

    if li == len(left):
        ans += right[ri:]
    else:
        ans += left[li:]

    return ans



if __name__ == '__main__':

    n = 20
    nums, test = list(range(n)), list(range(n))

    for i in range(100000):
        
        random.shuffle(nums)
        # print(nums)

        # bubble_sort(nums)
        # insertion_sort(nums)
        # selection_sort(nums)

        # shell_sort(nums)
        # HeapSort(nums).main()

        # QuickSort(nums).main(0, len(nums)-1)
        # nums = quick_sort_python(nums)
        nums = divide(nums)  # 归并排序

        # print(nums)
        # input()
        
        if nums != test:
            print(nums)
