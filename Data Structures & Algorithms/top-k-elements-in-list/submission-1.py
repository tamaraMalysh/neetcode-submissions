class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        count = Counter(nums)
        freq = [[] for i in range(len(nums) +1)]
        print(freq)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        print(freq)
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res