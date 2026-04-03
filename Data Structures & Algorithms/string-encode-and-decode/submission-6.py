class Solution:

    def encode(self, strs: List[str]) -> str:
        # if len(strs) == 0:
        #     return ""
        result = ""
        for s in strs:
            l = len(s)
            result = result+str(l)+"#"+s
        return result


    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        print(s)
        i = 0
        length = ""
        result = []
        while i < len(s):
            if s[i] == "#":
                # print(length)
                end = i+int(length)+1
                result.append(s[i+1:end])
                i = end
                length = ""
            else:
                length += s[i]
                # print(length, i)
                i +=1
        return result

        
