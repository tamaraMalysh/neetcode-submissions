class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_closing_map = {
            "{": "}",
            "[": "]",
            "(": ")",
        }
        for p in s:
            if p in open_closing_map.keys():
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                opening = stack.pop()
                if open_closing_map[opening] != p:
                    return False
        
        return len(stack) == 0