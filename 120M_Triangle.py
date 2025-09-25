class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        sums = []
        for i in range(len(triangle)):
            sums.append(1000)
            for j in range(len(triangle[i])-1, -1, -1):
                if i ==0:
                    sums[j] = triangle[i][j]
                else:
                    sums[j] = min(sums[j]+triangle[i][j], sums[max(j-1, 0)]+triangle[i][j])

        return min(sums)