class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        byte = bin(num)[2:]
        ret = ''
        for c in byte:
            if c == '1':
                ret += '0'
            else:
                ret += '1'

        return int(ret, 2)