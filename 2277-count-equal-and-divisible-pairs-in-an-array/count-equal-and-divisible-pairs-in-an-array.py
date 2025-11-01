class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = defaultdict(list)
        count = 0

        for i in range(len(nums)):
            v = nums[i]
            if v in h:
                for prev_i in h[v]:
                    if (i * prev_i) % k == 0:
                        count += 1
            h[v].append(i)
        
        return count

        