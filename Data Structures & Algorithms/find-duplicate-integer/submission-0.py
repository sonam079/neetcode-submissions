class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] = 1 + count[num]
        
        for key, value in count.items():
            if value > 1:
                return key
        