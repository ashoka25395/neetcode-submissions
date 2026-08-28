class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count_map={}
        for ch in s:
            count_map[ch] = count_map.get(ch,0)+1

        for ch in t:
            if ch in count_map:
                count_map[ch] = count_map[ch]-1  
            else:
                return False

        for ch in count_map:
            if count_map[ch] != 0:
                return False


        return True  



        