
def calculateMinimumHP(dungeon) -> int:
    # get dimensions
    m = len(dungeon)
    n = len(dungeon[0])

    # H[i][j] is min health needed to enter room (i, j) and stay alive in optimal path
    H = [[float('inf')]*n for _ in range(m)]

    # initialize bottom-right corner

    # minimum health to enter:
    # the minimum prev_health we need to enter should leave us with next_health = 1
    # prev_health + dungeon[i][j] = next_health --> prev_health = next_health - dungeon[i][j]

    # minimum health to still be alive:
    # we also need prev_health > 1 --> prev_health = max(next_health - dungeon[i][j], 1)

    H[-1][-1] = max(1-dungeon[-1][-1], 1)

    # initialize most-right column
    for i in range(m-2, -1, -1):
        # we have to move down if we're in the most-right column
        # recall: prev_health = max(next_health - dungeon[i][j], 1)
        H[i][-1] = max(H[i+1][-1] - dungeon[i][-1], 1)

    # initialize bottom row
    for j in range(n-2, -1, -1):
        # we have to move right if we're in the bottom row
        # recall: prev_health = max(next_health - dungeon[i][j], 1)
        H[-1][j] = max(H[-1][j+1] - dungeon[-1][j], 1)

    # compute rest
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            # needed health to go down
            d_sum = max(H[i+1][j] - dungeon[i][j], 1)

            # needed health to go right
            r_sum = max(H[i][j+1] - dungeon[i][j], 1)

            # health needed to enter next room on optimal path
            H[i][j] = min(d_sum, r_sum)

    # health needed for optimal path starting at (0, 0)
    return H[0][0]