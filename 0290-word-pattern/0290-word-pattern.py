class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # cho 2 for tách biệt
        # tạo dictionary với key là character còn val là word
        # trong quá trình tạo char nếu char đã tồn tại thì lấy word của char đó ra, so sánh với
        # cái word hiện tại
        # nếu không có thì thêm vào dict
        # nếu có rồi thì return false 

        # đặt 2 dict : w2c và c2w
        c2w = {}
        w2c = {}  
        words = s.split()
        if len(pattern) != len(words):
            return False        
      
        for i in range(len(pattern)):
            c = pattern[i]
            w = words[i]
            if c in c2w:
                if c2w[c] != w:
                    return False
            else:
                c2w[c] = w
            if w in w2c:
                if w2c[w] != c:
                    return False
            else:
                w2c[w] = c
        return True