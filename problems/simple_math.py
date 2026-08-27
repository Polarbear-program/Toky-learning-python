class Solution:
    def __init__(self, num_1, num_2):
        self.num = num_1
        self.num_2 = num_2

    def pow(num: int, num_pow: int):

        if num_pow == 0:
            return 1

        for times in range(num_pow-1):
            num *= num
        return num

    def sqrt(num_sqrt: float):

        if num_sqrt == 0:
            return 1

        return num_sqrt ** 0.5


a = 4
b = 2

print(Solution.sqrt(a))
