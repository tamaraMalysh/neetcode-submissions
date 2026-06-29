class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2
            guess_h = sum(math.ceil(p / mid) for p in piles)
            print(guess_h)
            if guess_h <= h:
                r = mid
            else:
                l = mid + 1

    
        return l