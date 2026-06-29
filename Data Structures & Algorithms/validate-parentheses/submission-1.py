class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_closing_map = {
            "{": "}",
            "[": "]",
            "(": ")",
        }
        for p in s:
            if p in open_closing_map:
                stack.append(p)
            elif stack and p == open_closing_map[stack[-1]]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0