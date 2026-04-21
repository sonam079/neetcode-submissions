class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_nums = 1
        zero_count = 0

        for n in nums:
            if n:
                prod_nums *= n
            else:
                zero_count += 1
        
        if zero_count > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        
        
        for i, c in enumerate(nums):
            if zero_count: res[i] = 0 if c else prod_nums
            else: res[i] = prod_nums // c

        return res
        