class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = 1+d.get(n, 0)
        
        frequencyList =[[] for _ in range(len(nums)+1)]

        print(d)
        for key, val in d.items():
            frequencyList[val].append(key)
        res = []
        
        for i in range(len(frequencyList)-1, 0, -1):
            for n in frequencyList[i]:
                res.append(n)
                if len(res) == k:
                    return res
        

        
        