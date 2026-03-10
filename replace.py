class Solution:
    def replaceElements(self, arr):
        max_right = -1

        for i in range(len(arr)-1, -1, -1):
            current = arr[i]
            arr[i] = max_right
            max_right = max(max_right, current)

        return arr


arr = [2,4,5,3,1,2]

sol = Solution()
print(sol.replaceElements(arr))
