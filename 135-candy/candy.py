class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [0] * len(ratings)
        candies[0] = 1
        for i in range(len(ratings)):
            if i + 1 != len(ratings):
                if ratings[i] < ratings[i + 1]:
                    candies[i + 1] = candies[i] + 1
                elif ratings[i] > ratings[i + 1] and candies[i] - 1 == 0:
                    candies[i] += 1
                    candies[i + 1] += 1
                else:
                    candies[i + 1] = 1

        for i in range(len(ratings) - 1, -1,-1):
            if i - 1 != -1:
                if ratings[i] < ratings[i - 1] and candies[i - 1] <= candies[i]:
                    candies[i - 1] = candies[i] + 1
        print(candies)
        return sum(candies)
