class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)-1
        if len(arr) < 3:
            return False
        i, j = 0,n
        while i < n and arr[i] < arr[i + 1]:
            i += 1
        while j >= 0 and arr[j] < arr[j - 1]:
            j -= 1
        return i == j and i != 0 and j != n