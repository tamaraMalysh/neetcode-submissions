class Solution:

    def encode(self, strs: List[str]) -> str:
        # res = ""
        # for s in strs:
        #     res += str(len(s)) + "#" + s
        return "".join([f"{len(s)}${s}" for s in strs])
    def decode(self, s: str) -> List[str]:
        print(s)
        i = j = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "$":
                j +=1
                
            s_len = int(s[i:j])

            i = j + 1
            j = i + s_len
            res.append(s[i:j])
            print(res)
            i = j
        return res

