from functools import reduce

my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums1 = reduce(lambda x, y: x + 1, my_nums)
print(nums1)
