from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashy={}
        output=[]
        for n in nums:
            if n not in hashy:
                hashy[n]=1
            else:
                hashy[n]+=1
        for numbers,count in hashy.items():
            output.append([count,numbers])
        output.sort(reverse=True)
        fw=[]
        for i in range(k):
            wi=output[i][1]
            fw.append(wi)
        return fw
        