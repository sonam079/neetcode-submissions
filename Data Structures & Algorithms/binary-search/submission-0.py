class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, low, high, target):
            if low > high:
                return -1

            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                high = mid - 1
                return binary_search(nums, low, high, target)
            else:
                low = mid + 1
                return binary_search(nums, low, high, target)
        
        low, high = 0, len(nums) - 1
        return binary_search(nums, low, high, target)