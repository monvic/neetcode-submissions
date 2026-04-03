class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dl = {}
        result = []
        for s in strs:
            ds = self.createList(s)
            if dl.get(ds) is None:
                dl[ds] = [s]
            else:
                dl.get(ds).append(s)
        for val in dl.values():
            result.append(val)
        return result

            

    
    def createList(self, s: str):
        l = [0]*26
        for c in s:
            index = ord(c)-97
            l[index] += 1
        return tuple(l)

        