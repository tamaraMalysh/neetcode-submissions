class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(
            f"{len(s)}#{s}" for s in strs
        )

    def decode(self, s: str) -> List[str]:
        res = []
        i = j = 0
        while i < len(s):
            while s[j] != "#":
                j+=1

            len_s = int(s[i:j])

            i = j + 1
            j = j + len_s + 1
            
            res.append(s[i:j])
            i = j
        
        return res