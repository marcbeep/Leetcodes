def merge (nums1, m, nums2, n):
    # Last index nums1
    last = m + n - 1

    # Merge in reverse order
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else: 
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1
    
    # Put all remaining elements in nums2 and attach to 
    # the beginning of nums1
    while n > 0:
        nums1[last] = nums2[n - 1]
        n, last = n - 1, last - 1
    
    return nums1

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = len(nums1) - len(nums2) # Ensure only the relevant elements of nums1 are considered
n = len(nums2)
merged = merge(nums1, m, nums2, n)
print(merged)
