import random
def quickselect(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("k должно быть от 1 до длины списка")
    t = len(nums) - k
    l = 0
    r = len(nums) - 1
    while l <= r:
        pivot_index = random.randint(l, r)
        pivot = nums[pivot_index]
        nums[pivot_index], nums[r] = nums[r], nums[pivot_index]

        store_index = l

        for i in range(l, r):
            if nums[i] < pivot:
                nums[i], nums[store_index] = nums[store_index], nums[i]
                store_index += 1
        nums[store_index], nums[r] = nums[r], nums[store_index]

        if store_index == t:
            return nums[store_index]
        elif store_index < t:
            l = store_index + 1
        else:
            r = store_index - 1
nums1 = [3, 2, 1, 5, 6, 4]
print(quickselect(nums1, 2))  # 5

nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
print(quickselect(nums2, 4))  # 4