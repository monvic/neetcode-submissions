class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        workingK = end
        while start <= end:
            mid = (start+end)//2
            time = sum(math.ceil(pile/mid) for pile in piles )


            if (time > h):
                start = mid + 1
            
            elif time <= h :
                end = mid - 1
                print(mid, workingK)
                workingK = min(mid, workingK)
            
        
        return workingK
        