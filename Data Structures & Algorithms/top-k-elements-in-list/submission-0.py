class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        res = []
        freq_map = defaultdict(int)
        for x in nums:
            freq_map[x]+=1
        
        for x in freq_map:
            heapq.heappush(h,(-freq_map[x],x))
        
        for i in range (0,k):
            res.append(heapq.heappop(h)[1])
        
        return res
            


        