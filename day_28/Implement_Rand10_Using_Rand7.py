# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # generate a random number between [1 : 40] with equal prob for each number
            random_num = (rand7()-1) * 7 + rand7()

            if random_num <= 40:
                # map [1 : 40] to [1 : 10] by modulo operation with offset
                return random_num % 10 + 1
