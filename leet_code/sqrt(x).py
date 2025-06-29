
class Solution:
    @staticmethod
    def mySqrt(x) -> int:
        low = 0
        high = x
        res = 1

        while low <= high:
            mid = int(low + ((high - low)/2))
            if mid * mid <= x:
                low = mid + 1
                res = mid
            else:
                high = mid - 1
        return res



if __name__ == '__main__':
    input = 9
    print(Solution.mySqrt(input))
    # output = Square root of x

