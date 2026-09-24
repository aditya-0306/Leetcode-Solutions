

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to minimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2
        
        while left <= right:
            i = (left + right) // 2
            j = half_len - i
            
            max_left_x = float('-inf') if i == 0 else nums1[i - 1]
            min_right_x = float('inf') if i == m else nums1[i]
            
            max_left_y = float('-inf') if j == 0 else nums2[j - 1]
            min_right_y = float('inf') if j == n else nums2[j]
            
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # Correct partition found
                if (m + n) % 2 == 1:
                    return max(max_left_x, max_left_y)
                else:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
            elif max_left_x > min_right_y:
                right = i - 1
            else:
                left = i + 1
                
        raise ValueError("Input arrays are not sorted or invalid.")
        