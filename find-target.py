class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        d=[]
        if(target not in nums):
            return d
        else:
            e=0
            while(target in nums):
                d.append(nums.index(target)+e)
                nums.remove(target)
                e+=1
        return d
