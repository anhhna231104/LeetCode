class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if timeSeries is None:
            return 0
        i = 1
        sum = 0
        # while i < len(timeSeries):
        #     if timeSeries[i]-timeSeries[i-1] < duration:
        #         sum+=timeSeries[i]-timeSeries[i-1]
        #     else:
        #         sum+=duration
        #     i+=1
        # sum+=duration
        for i in range(1,len(timeSeries)):
            if timeSeries[i]-timeSeries[i-1] < duration:
                sum+=timeSeries[i]-timeSeries[i-1]
            else:
                sum+=duration
        sum+=duration
        return sum

        