class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            if d.get(c) is None:
                d[c] = 1
            else:
                d[c] += 1
        
        for c in t:
            if d.get(c) is None:
                return False
            else:
                d[c] -= 1
        
        for key in [*d]:
            if d[key] != 0:
                return False
        
        return True
        