class Solution(object):
    def BinSearch(self, arr, target):
        left,right = 0,len(arr)-1
        while left<=right:
            mid = (left+right)//2
            if arr[mid] < target:
                left = mid+1                
            elif arr[mid] > target:
                right = mid-1
            else:
                return mid
        return -1
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr_sorted = sorted(arr)
        for i in range(len(arr_sorted)):
            flag = self.BinSearch(arr_sorted, 2*arr_sorted[i])
            if flag != -1 and flag != i:
                return True
        return False
        