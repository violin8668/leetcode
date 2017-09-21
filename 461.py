import sys,os


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        byteX, byteY = bin(x)[2:], bin(y)[2:]
        num = 0

        print byteX, byteY
        i = -1
        while abs(i) <= min(len(byteX), len(byteY)):
            if byteX[i] != byteY[i]:
                num += 1

            i -= 1

        byte = byteX if len(byteX) > len(byteY) else byteY
        while abs(i) <= len(byte):
            if byte[i] == '1':
                num += 1

            i -= 1

        return num

    def hammingDistence2(self, x, y):
        cnt = 0
        while x != 0 and y != 0:
            if x%2 != y%2:
                cnt += 1
            x /= 2
            y /= 2

        while x != 0:
            if x%2:
                cnt += 1
            x /= 2

        while y != 0:
            if y%2:
                cnt += 1
            y /= 2

        return cnt


if __name__ == "__main__":
    obj = Solution()
    print obj.hammingDistance(1, 4)
    print obj.hammingDistence2(0, 1)