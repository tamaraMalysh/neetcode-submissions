class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = set(nums)
        res = 0
        for n in nums:
            if n-1 not in hash_map:
                seq = 0
                while (n + seq) in hash_map:
                    seq +=1
                res = max(res, seq)

        return res
