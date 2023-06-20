def count_continents(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 1 and not visited[x][y]
    def expose_neighbours(x, y):
        visited[x][y] = True
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                expose_neighbours(new_x, new_y)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                expose_neighbours(i, j)
                count += 1

    return count

matrix = [
    [1, 1, 0, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1],
]

continent_count = count_continents(matrix)
print("Number of continents:", continent_count)
