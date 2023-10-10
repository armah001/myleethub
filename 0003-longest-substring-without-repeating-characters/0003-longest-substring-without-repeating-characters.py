class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left, right = 0, 1
        startIdx = 0 
        seen = {}

        for idx,char in enumerate(s):
            if char in seen:
                prevIdxOfRepeatingChar = seen[s[idx]]
                startIdx = max(startIdx, prevIdxOfRepeatingChar + 1)
                

            if right - left < idx - startIdx + 1:
                left = startIdx
                right = idx + 1
            
            seen[char] = idx
           
        return right - left


        # dic, res, start, = {}, 0, 0
        # for i, ch in enumerate(s):
        #     if ch in dic:
        #         res = max(res, i-start) # update the res
        #         start = max(start, dic[ch]+1)  # here should be careful, like "abba"
        #     dic[ch] = i
        # return max(res, len(s)-start)  # return should consider the last non-repeated substring

