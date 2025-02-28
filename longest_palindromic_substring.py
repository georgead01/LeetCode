def longestPalindrome(s: str) -> str:
        
        n = len(s)

        # D is an (n x n) matrix
        # the entry at (start, length) indicates whether the substring
        # of length 'length' starting at 'start' is palindromic. (Technically, 
        # substring of length row + 1 due to 0-based indexing).
        D = [[False for _ in range(n)].copy() for _ in range(n)]

        # All substrings of length 1 are palindromic.
        D[0] = [True for _ in range(n)]
        
        # A substring of length 2 is palindromic if both chars are the same.
        for i in range(n-1):
            if s[i] == s[i+1]:
                D[1][i] = True
        
        # A subatring of length 'length' starting at 'start' is palindromic only if
        # the substring of length 'length'-2 starting at 'start'-1 is palindrom AND
        # the two chars around are the same.
        for row in range(2, n):
            sub_len = row + 1
            if sub_len % 2:
                for col in range(n-row):
                    D[row][col] = D[row-2][col + 1] and s[col] == s[col + row]
            else:
                for col in range(n-row):
                    D[row][col] = D[row-2][col + 1] and s[col] == s[col + row]

        # We find the first True value starting from the bottom of the matrix D.
        for row in range(n-1, -1, -1):
            for col in range(n):
                if D[row][col]:
                    return s[col: col+row+1]

        # This algorithm is of time complexity O(n^2). Constucting the matrix D takes
        # O(n^2) and then populating each entry takes O(1) for O(n^2) entries.