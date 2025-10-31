class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        if k == 0:
            return [0] * len(code)
        
        res = []
        for i in range(len(code)):
            if k > 0:
                sum = 0 
                j = i + 1
                tmp = k

                while tmp:
                    sum += code[j % len(code)]
                    j += 1
                    tmp -= 1
                res.append(sum)

            else:
                sum = 0
                j = i -1
                tmp = k

                while tmp:
                    sum += code[j % len(code)]
                    j -= 1
                    tmp += 1
                res.append(sum)
                
        return res

                    


