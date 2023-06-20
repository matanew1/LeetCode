class Solution(object):
    def binary_search(self, arr, start, end, target):
        median = (start + end) // 2

        if start > end or median == target == 0:
            return -1
        if target == arr[median]:
            return median
        elif target > arr[median]:
            return self.binary_search(arr, median + 1, end, target)
        else:
            return self.binary_search(arr, start, median - 1, target)


    def searchMatrix(self, matrix, target):
        arr = [element
               for arr in matrix
                    for element in arr]
        if self.binary_search(arr, 0, len(arr) - 1, target) != -1:
            return True
        return False

solution = Solution()
print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 0))