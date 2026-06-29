class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target_counter = Counter(s1)  
        window_counter = Counter(s2[:len(s1)])

        if target_counter == window_counter:
            return True

        for i in range(len(s1),len(s2)):
            start_symbol = s2[i-len(s1)]
            end_symbol = s2[i]
            window_counter[start_symbol] -=1
            window_counter[end_symbol] +=1

            if window_counter[end_symbol] == 0:
                del window_counter[end_symbol]

            if target_counter == window_counter:
                return True

        return False