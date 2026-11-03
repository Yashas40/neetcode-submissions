class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        repMap={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in repMap:
                return [repMap[complement],i]
            repMap[num]=i
        return[]