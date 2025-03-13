def dividePlayers(skill) -> int:
    # idea: lowest skill must be paired with highest skill if
    # skill pairs are to be equal. Once paired, it is true for the 
    # remaining players.

    # Runtime: O(n log n), assuming merge sort

    skill.sort()

    team_skill = skill[0]+skill[-1]

    n = len(skill)

    chem = 0

    for i in range(n//2):
        s1 = skill[i]
        s2 = skill[n-i-1]

        if s1+s2 != team_skill:
            return -1
        
        chem += s1*s2

    return chem