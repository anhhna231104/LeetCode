class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, i = 0, 1   
        prev = nums[0]

        for i in range(1, len(nums) - 1):
            nxt = nums[i + 1]
            if prev == nums[i]:
                continue
            if nums[i] == nxt:
                continue

            if prev < nums[i] and nxt < nums[i]:
                count += 1            
            elif prev > nums[i] and nxt > nums[i]:
                count += 1           

            prev= nums[i]

        return count
