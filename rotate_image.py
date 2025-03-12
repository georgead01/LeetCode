def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    # get dimensions of matrix
    n = len(matrix)

    # rotate 90 deg clockwise = trasnpose -> mirror verically
    
    ### transpose ###

    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    ### mirror ###
    
    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]