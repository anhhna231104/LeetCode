class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        words = sentence.split()
        goat_latin = []
        for i,w in enumerate(words):
            if w[0].lower() in vowels:
                goat = w +'ma'
            else:
                goat = w[1:] + w[0] + 'ma'
            goat+='a'*(i+1)
            goat_latin.append(goat)
        return ' '.join(goat_latin)



        