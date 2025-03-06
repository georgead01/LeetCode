def canCompleteCircuit(gas, cost) -> int:
    
    n = len(gas)

    # if the total difference between gas and cost is negative
    # we can't make a full circle starting anywhere
    diff = [gas[idx]-cost[idx] for idx in range(n)]
    if sum(diff) < 0:
        return -1

    # if I start at a and get stuck at b, I can't get to b (or will get stuck)
    # from any point between a and b. Why? because I would have 0 or more gas in the
    # tank coming into any of these stations, and I still got stuck.

    # we set start to 0 and an empty tank
    start = 0
    tank = 0

    idx = 0
    while idx < n:
        tank += gas[idx]
        # if enough gas in tank, go to the next station
        if tank >= cost[idx]:
            tank -= cost[idx]
            idx += 1
        # if not, none of the stations between the prev defined start and
        # this station can be considered for a starting point, so we set the next point
        # to the next station with non-negative gas-cost difference.
        else:
            while gas[idx]-cost[idx] <= 0:
                idx += 1
            # once we found the next non-negative difference station, set as
            # the new start, and empty tank
            start = idx
            tank = 0
    
    return start

    # This algorithm is O(n) as each index is visited only once, and calculating
    # difference and start take O(n) each as well.