class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        result = []
        if numerator * denominator < 0:
            result.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)
        result.append(str(numerator // denominator))  # integer part
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)
        result.append(".")

        remainders = {}
        while remainder != 0:
            if remainder in remainders:
                result.insert(remainders[remainder], "(")
                result.append(")")
                return "".join(result)
            remainders[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
        return "".join(result)


sol = Solution()
print(sol.fractionToDecimal(0, 3))
