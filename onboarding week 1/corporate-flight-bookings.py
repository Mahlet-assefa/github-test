class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans=[0]*(n+1)
        for first,last,seats in bookings:
            ans[first-1] += seats
            ans[last] -= seats
        for first in range(1, len(ans)):
            ans[first] += ans[first-1]
        ans.pop()
        return ans
