class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for i in s:
                arr[ord(i)-ord("a")] += 1
            c = tuple(arr)
            seen[c].append(s)

        return list(seen.values())
