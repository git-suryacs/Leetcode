class Solution:
    def runningSum(self, nums):
        result=[]
        temp = 0
        for i in range(len(nums)):
            result.append(nums[i]+temp)
            temp = nums[i]+temp
        return result

    
s=Solution()
print(s.runningSum(nums=[1,2,3,4,5]))
            