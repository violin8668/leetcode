class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        ret = []
        for word in words:
            tmp = word.lower()
            flag = line[0]
            for i in range(3):
                print tmp[0]
                if tmp[0] in line[i]:
                    flag = line[i]
                    break

            i = 1
            print flag
            while i < len(word):
                if tmp[i] not in flag:
                    break
                i += 1
            if i == len(word):
                ret.append(word)

        return ret

    def findWords2(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        ret = []
        for word in words:
            if set(word.lower()).issubset(line1) or set(word.lower()).issubset(line2) or set(word.lower()).issubset(line3):
                ret.append(word)

        return ret


if __name__ == "__main__":
    obj = Solution()
    print obj.findWords2(["Hello", "Alaska", "Dad", "Peace"])