class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, len(s)-1
        res = 0
        while start <= end:
            seen = set()
            i = start
            while i <= end:
                if s[i] not in seen:
                    seen.add(s[i])
                    i+=1
                else:
                    break
            res = max(res, len(seen))
            start +=1

        return res
