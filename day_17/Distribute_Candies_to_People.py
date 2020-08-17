def distributeCandies(candies: int, num_people: int) -> [int]:
    rnd = 0
    res = [0 for _ in range(num_people)]
    while candies:
        for i in range(num_people):
            if not candies:
                break
            required_candies = (num_people * rnd) + i + 1
            if required_candies <= candies:
                res[i] += required_candies
                candies -= required_candies
            else:
                res[i] += candies
                candies = 0
        rnd += 1
    return res


print(distributeCandies(7, 4))
