class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in xrange(m - 1, -1, -1):
            d1 = ord(num1[i]) - ord('0')
            for j in xrange(n - 1, -1, -1):
                d2 = ord(num2[j]) - ord('0')

                mul = d1 * d2
                p1, p2 = i + j, i + j + 1

                total = mul + result[p2]

                result[p2] = total % 10
                result[p1] += total // 10
        start = 0
        while start < len(result) - 1 and result[start] == 0:
            start += 1

        digits = result[start:]
        return ''.join(str(d) for d in digits)
