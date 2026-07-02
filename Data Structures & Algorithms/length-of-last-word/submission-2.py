class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1 and s:
            return 1
        ans = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                i -= 1
            if s[i] != " ":
                while i < len(s) and s[i] != " ":
                    ans += 1
                    i -= 1
            if ans > 0:
                break
        return ans
        