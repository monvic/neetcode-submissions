class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        result = [0] * len(temperatures)
        for i, val in enumerate(temperatures):
            while s and temperatures[s[-1]] < val:
                # print(s, val, temperatures[s[-1]])
                ti = s.pop()
                result[ti] = i - ti
                # print(result)
                
            s.append(i)
            # print(s)
        while s:
            i = s.pop()
            # print(i)
            # print(result)
            result[i] = 0
        return result

    
