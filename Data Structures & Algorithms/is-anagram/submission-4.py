class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for j in t:
            if j in s:
                dic[j]-=1
            else:
                return False
        for count in dic.values():
            if count!=0:
                return False
        return True