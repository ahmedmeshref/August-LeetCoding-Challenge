# sort nums array performing a series of pancake flips.
def pancakeSort(nums: [int]) -> [int]:
    out = []

    def flip(ind):
        out.append(ind)
        for i in range(ind // 2):
            nums[i], nums[ind - i - 1] = nums[ind - i - 1], nums[i]

    for num in range(len(nums), 0, -1):
        k = nums.index(num) + 1
        if k == num:
            continue
        elif k == 1:
            flip(num)
        else:
            flip(k)
            flip(num)
    return out