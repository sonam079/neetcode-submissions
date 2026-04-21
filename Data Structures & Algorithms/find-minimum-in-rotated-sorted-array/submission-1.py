class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                return res
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                # the left half of array is sorted, search in right half
                l = m + 1
            else:
                r = m - 1
        return res
        