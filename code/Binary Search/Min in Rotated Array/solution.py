/*
This sketch implements binary search on a rotated 1-D array

*/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while high > low:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[high] > nums[mid]:
                high = mid
        return nums[low]
            
