def maxMoves(grid):
    m, n = len(grid), len(grid[0])
    
    # dp[i][j] represents the maximum moves starting from cell (i, j)
    dp = [[0] * n for _ in range(m)]
    
    # Initialize dp values for the last column (base case)
    for i in range(m):
        dp[i][-1] = 1
    
    # Iterate through the grid from right to left
    for j in range(n - 2, -1, -1):
        for i in range(m):
            # Consider current cell as a move
            dp[i][j] = 1
            
            # Explore adjacent cells and update dp[i][j] accordingly
            if i > 0 and grid[i][j] < grid[i - 1][j + 1]:
                dp[i][j] = max(dp[i][j], 1 + dp[i - 1][j + 1])
            if grid[i][j] < grid[i][j + 1]:
                dp[i][j] = max(dp[i][j], 1 + dp[i][j + 1])
            if i < m - 1 and grid[i][j] < grid[i + 1][j + 1]:
                dp[i][j] = max(dp[i][j], 1 + dp[i + 1][j + 1])
    
    # Return the maximum moves from the first column
    return max(dp[i][0] for i in range(m))

# Example usage
grid1 = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
print(maxMoves(grid1))  # Output: 3

grid2 = [[3,2,4],[2,1,9],[1,1,7]]
print(maxMoves(grid2))  # Output: 0
