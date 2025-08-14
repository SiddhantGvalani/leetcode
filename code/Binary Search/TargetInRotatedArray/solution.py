class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        while high >= low:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[low]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if target <= nums[mid] or target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1
            
            
            
            
            
            
            
            
            
            
