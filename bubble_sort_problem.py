
## Bubble Sort

def BubbleSort(nums):
    n = len(nums)
    swaps_num = 0
    
    for i in range(n):
        swapped = True
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
                swaps_num += 1
        if not swapped:
            break
    print(f"Array is sorted in {swaps_num} swaps.")
    print(f"First Element: {nums[0]}")
    print(f"Last Element: {nums[-1]}")
    return nums


n = int(input())

a = list(map(int,input().rstrip().split()))

BubbleSort(a)
