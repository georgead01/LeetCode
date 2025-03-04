def canJump(nums) -> bool:
    
    n = len(nums)

    # if the list is of length 1 or less, the game is solved
    if n <= 1:
        return True

    # the farthest reached
    end = 0
    for idx in range(n):
        # if idx is unreachable, return false
        if end < idx:
            return False
        # if idx can reach beyond end, update
        if idx + nums[idx] > end:
            end = idx + nums[idx]

    # return whether n-1 is reachable
    return end >= n-1

    # This algorithm is O(n).