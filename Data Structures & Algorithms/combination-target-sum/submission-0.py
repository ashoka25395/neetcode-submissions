class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        subset = []

        def dfs(idx, currSum):
            if currSum == target:
                res.append(subset.copy())
                return 
            
            if idx>=len(nums) or currSum >target:
                return 

            subset.append(nums[idx])
            dfs(idx, currSum+nums[idx])
            subset.pop()
            dfs(idx+1, currSum)


        dfs(0, 0)
        return res

                

        