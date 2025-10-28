class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i,n = 0,len(arr)-1
        while(i<n):
            if(arr[i]==0):
                arr.insert(i+1,0)
                arr.pop()
                i+=1
            i+=1
            #test pushing github
        