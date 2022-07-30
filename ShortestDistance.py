# Shortest path for current location and distance
# from source location
class ShortestPath:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist

    def __repr__(self):
        return f"ShortestPath({self.row}, {self.col}, {self.dist})"


def min_Distance(grid):
    source = ShortestPath(0, 0, 0)

    # Finding the source to start from
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'A':
                source.row = row
                source.col = col
                break

    # To maintain location visit status
    visited = [[False for _ in range(len(grid[0]))]
               for _ in range(len(grid))]

    # applying breadth first search on matrix cells starting from source
    queue = []
    queue.append(source)
    visited[source.row][source.col] = True
    while len(queue) != 0:
        source = queue.pop(0)

        # Destination B found;
        if grid[source.row][source.col] == 'B':
            return source.dist

        # moving up
        if isValid(source.row - 1, source.col, grid, visited):
            queue.append(ShortestPath(source.row - 1, source.col, source.dist + 1))
            visited[source.row - 1][source.col] = True

        # moving down
        if isValid(source.row + 1, source.col, grid, visited):
            queue.append(ShortestPath(source.row + 1, source.col, source.dist + 1))
            visited[source.row + 1][source.col] = True

        # moving left
        if isValid(source.row, source.col - 1, grid, visited):
            queue.append(ShortestPath(source.row, source.col - 1, source.dist + 1))
            visited[source.row][source.col - 1] = True

        # moving right
        if isValid(source.row, source.col + 1, grid, visited):
            queue.append(ShortestPath(source.row, source.col + 1, source.dist + 1))
            visited[source.row][source.col + 1] = True

    return -1


# checking where valid or not move
def isValid(x, y, grid, visited):
    if ((x >= 0 and y >= 0) and
            (x < len(grid) and y < len(grid[0])) and
            (grid[x][y] != '0') and (visited[x][y] == False)):
        return True
    return False


# Driver code
if __name__ == '__main__':
    grid = [['0', '#', '0', '#'],
            ['#', '0', '#', 'B'],
            ['0', '#', '#', '#'],
            ['A', '#', '#', '#']]

    print(min_Distance(grid))
