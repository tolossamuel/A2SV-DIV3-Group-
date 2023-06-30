class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d=[]
        e=0
        for i in range(len(nums)):
            for y in range(len(nums)):
                if(nums[i]>nums[y]):
                    e+=1
            d.append(e)
            e=0
        return d
