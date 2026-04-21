class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            word_sorted = "".join(sorted(word))
            res[word_sorted].append(word)
        return list(res.values())


        

        