from collections import deque


class Solution:
    def sortArrayByParity(self, A: [int]) -> [int]:
        parity_d = deque()
        for num in A:
            if num % 2:
                # odd number
                parity_d.append(num)
            else:
                parity_d.appendleft(num)
        return parity_d


