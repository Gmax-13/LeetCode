class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to minimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2
        
        while left <= right:
            # i partitions nums1, j partitions nums2
            i = (left + right) // 2
            j = half_len - i
            
            # Boundary conditions: handle edges when partitions are empty
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]
            
            # Check if we found the correct partition point
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # If total length is odd, median is the maximum of the left halves
                if (m + n) % 2 == 1:
                    return float(max(nums1_left_max, nums2_left_max))
                # If total length is even, median is average of middle boundaries
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
            
            # nums1's left side is too big; move partition i to the left
            elif nums1_left_max > nums2_right_min:
                right = i - 1
            # nums1's left side is too small; move partition i to the right
            else:
                left = i + 1
                
        return 0.0
