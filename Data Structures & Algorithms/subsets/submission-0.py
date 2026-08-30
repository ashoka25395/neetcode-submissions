class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(idx, subset):
            if idx >= len(nums):
                res.append(subset.copy())
                return 
            
            dfs(idx+1, subset)
            subset.append(nums[idx])
            dfs(idx+1, subset)
            subset.pop()
        
        dfs(0, [])
        return res



        