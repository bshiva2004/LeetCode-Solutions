class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        count=[]
        freq={}
        for num in nums:
            freq[num] = freq.get(num,0)+1


        for num in nums:
            if freq[num] == 1:
                count.append(num)
        return count            