class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted([s1 for s1 in s]) == sorted([s2 for s2 in t])