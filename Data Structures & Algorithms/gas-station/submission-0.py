class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

    # 0 + 3 - 2 = 1 # gas left after traveling from 2 -> 0
    # 1 + 1 -2 = 0 # gas left after traveling from  0 -> 1
    # 0 + 2 - 3 = -1 # gas left after traelin from 1 -> 2

# -2+0-1 = -3
# 3
        curr_starting = 0
        discarded_sum = 0

        total = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i] # the amount remaining in tank to go from i -> i+1

            # now if this remaining amount < 0, it means we can't move forward ahead beyond i+1 so we have to start from the next one. if its < 0, so the amount in tank is not enough to move ahead.
            if total < 0:
                discarded_sum += total # we keep running total of whwat we didnt consider. 
                total = 0 # we reset it
                curr_starting = i + 1 # we consider from the next one, cause in next iteration we directly calcuale how much to grom next to next one.

        if total + discarded_sum >= 0:
            # we had enough in tank to cover the discated one too
            return curr_starting
        else:
            return -1
            