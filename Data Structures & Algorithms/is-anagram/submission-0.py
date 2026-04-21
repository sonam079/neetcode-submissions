class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping_1 = {}
        mapping_2 = {}

        for char in s:
            if char in mapping_1:
                mapping_1[char] += 1
            else:
                mapping_1[char] = 1
        
        for char in t:
            if char in mapping_2:
                mapping_2[char] += 1
            else:
                mapping_2[char] = 1
        
        return mapping_1 == mapping_2