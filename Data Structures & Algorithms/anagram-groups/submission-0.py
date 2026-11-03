from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram=defaultdict(list)
        result=[]
        for s in strs:
            ss=tuple(sorted(s))
            anagram[ss].append(s)
        for value in anagram.values():
            result.append(value)
        return result