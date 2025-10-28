class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 

        closest = float('inf')
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = a + nums[l] + nums[r]
                curr_dist = abs(target - total)
                closest_dist = abs(target - closest)

                if curr_dist < closest_dist:
                    closest = total
                
                if total == target:
                    return total
                elif total > target: 
                    r -= 1
                else:
                    l += 1
                
        return closest
        