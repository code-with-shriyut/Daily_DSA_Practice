# LEETCODE 933: Number of Recent Calls

# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:
# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, 
# and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). 
# Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

# Example 1:

# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]

# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

class RecentCounter:

    def __init__(self):

        # Queue to store the time of every recent request
        self.queue = deque()

    def ping(self, t):
        """
        :type t: int
        "rtype: int
        """

        # Add the current request time to the queue
        self.queue.append(t)

        # Remove all requests that are older than (t - 3000)
        # because they are no longer inside the current time window
        while self.queue[0] < t - 3000:
            self.queue.popleft()

        # The remaining requests are within [t - 3000, t]
        # so the size of the queue is our answer
        return len(self.queue)

# Time Complexity: O(1) Amortized
# - Each request is added to the queue once.
# - Each request is removed from the queue at most once.
# - Therefore, the average work per ping() is O(1).

# Space Complexity: O(n)
# - In the worst case, all recent requests remain in the queue.
    

