class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repMap={}
        for i,num in enumerate(nums):
            if num not in repMap:
                repMap[num]=1
            else:
                repMap[num]+=1
                return True
        return False