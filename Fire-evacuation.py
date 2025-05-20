movements = [( -1,0), (1,0), (0,-1), (0,1)]
empty_cost = 1
smoke_cost = 3
fire_cost = float('inf')
spread_delay = 1
grid = """
.  .  .  F  .  .  .  E  .  .
.  X  X  .  X  X  .  .  .  .
.  .  .  .  .  .  .  .  .  .
.  .  .  S  .  .  X  .  .  .
.  .  X  S  .  .  .  .  .  .
X  .  .  .  X  .  .  .  .  .
.  .  .  .  .  X  .  P  .  .
.  .  .  .  X  .  .  .  .  .
.  .  .  .  .  .  .  .  .  .
E  .  .  .  .  .  .  P  .  .
"""
full_grid = [list(line.replace(" ",""))for line in grid.strip().split('\n')]
class Person:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def bfs(start):
    visited = [[False] * 10 for _ in range(10)]
    queue = [(start.x, start.y, 0)]
    visited[start.x][start.y] = True
    while queue:
        x, y, steps = queue.pop(0)
        if full_grid[x][y] == 'E':
            return steps
        for node_x, node_y in movements:
            new_x, new_y = x + node_x, y + node_y
            if 0 <= new_x < 10 and 0 <= new_y < 10 and not visited[new_x][new_y]:
                if full_grid[new_x][new_y] !='X' and full_grid[new_x][new_y] != 'F':
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y, steps + 1))
    return None
def UCS(start):
    priority_queue = [(start.x, start.y, 0)]
    visited = [[False] * 10 for _ in range(10)]
    cost_map = [[float('inf')] * 10 for _ in range(10)]
    cost_map[start.x][start.y] = 0
    while priority_queue:
        priority_queue.sort()
        x, y, cost = priority_queue.pop(0)
        if full_grid[x][y] == 'E':
            return cost
        if visited[x][y]:
            continue
        else:
            visited [x][y] = True
            for node_x, node_y in movements:
                new_x, new_y = x + node_x, y + node_y
                if 0 <= new_x < 10 and 0 <= new_y < 10:
                    if full_grid[new_x][new_y] != 'X' and (cost + (smoke_cost if full_grid[new_x][new_y] == 'S' else empty_cost)) < cost_map[new_x][new_y]:
                        new_cost = cost + (smoke_cost if full_grid[new_x][new_y] == 'S' else empty_cost)
                        priority_queue.append((new_x, new_y, new_cost))
                        cost_map[new_x][new_y] = new_cost

def fire_spread(grid):
    fire_nodes = []
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'F':
                fire_nodes.append((i,j))
    new_grid = [row[:] for row in grid]
    for x, y in fire_nodes:
        for node_x, node_y in movements:
            new_x, new_y = x + node_x, y + node_y
            if 0 <= new_x < 10 and 0 <= new_y < 10:
                if new_grid[new_x][new_y] == '.':
                    new_grid[new_x][new_y] = 'S'
    return new_grid
def simulate(full_grid):
    people = []
    exits = []
    for i in range(10):
        for j in range(10):
            if full_grid[i][j] == 'P':
                people.append(Person(i, j))
            elif full_grid[i][j] == 'E':
                exits.append((i, j))
   
    full_grid = fire_spread(full_grid)
    for person in people:
        steps_bfs = bfs(person)
        print(f"Person at ({person.x}, {person.y}) BFS steps: {steps_bfs}")

        cost_ucs = UCS(person)
        print(f"Person at ({person.x}, {person.y}) UCS cost: {cost_ucs}")
            
simulate(full_grid)
