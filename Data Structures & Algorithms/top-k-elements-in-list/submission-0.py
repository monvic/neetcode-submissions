class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if d.get(n) is None:
                d[n] = 1
            else:
                d[n] += 1
        
        di = d.items()
        diSorted = sorted(di, key = lambda i: i[1], reverse = True)
        print(diSorted)
        result = []
        for i in range(0, k):
            result.append(diSorted[i][0])

        return result
            

        