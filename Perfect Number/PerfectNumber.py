class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 0
        for x in range(num):
            if num % x == 0:
                sum = sum + x
        if sum == num:
            return True