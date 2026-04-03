class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [x*-1 for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            diff = abs(stone1 - stone2)
            if diff != 0:
                heapq.heappush(stones,diff * -1)
        
        if len(stones) == 0:
            return 0
        else:
            return stones[0] * -1




        