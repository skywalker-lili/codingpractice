
# coding: utf-8

# In[51]:


# 16.19 Pond Sizes

# ---- Solution ----

# Helper function to find yet not visited adjacent pond, given a start point
def find_neighbour(Land,m,n,cell_cord):
    neibour_cord = set([])
    i = cell_cord[0]
    j = cell_cord[1]
    for x in [max(i-1, 0), i, min(i+1, m-1)]:
        for y in [max(j-1, 0), j, min(j+1, n-1)]:
            if (x, y) != (i, j):
                neibour_cord.add((x, y))
    return neibour_cord

# Helper function to BFS from a pond cell and return the pond size
# Along the way, updated visited ponds
def find_size_bfs(Land,m,n,cord,visited):
    size = 1 # start point is already visited
    i = cord[0]
    j = cord[1]
    pond = [(i, j)]
    while len(pond) > 0:
        cell_cord = pond.pop(0) # Acutally list is an array, better use collections.deque as a real queue
        # Only do stuff on the current cell
        # If this cell hasn't been visited, visit.
        # Notice cell_cord must be a water cell to be added in pond, so no need to check if it's water
        if cell_cord not in visited:
            visited.add(cell_cord)
            size += 1
        # Use the neibours to expand searching range, but don't actually do anything else so logic is clear
        for neibour_cord in find_neighbour(Land,m,n,cell_cord):
            if neibour_cord not in visited            and Land[neibour_cord[0]][neibour_cord[1]] == 0: # Only expand by water cell
                pond.append(neibour_cord)
    
    return size

# Main function
def pond_size(Land):
    # Scan each cell, when find a pond, BFS to find its size
    # Mark visited cells along the way to avoid re-visiting
    # O(mn) space and O(mn) time
    m = len(Land)
    if m == 0: return set([])
    n = len(Land[0])
    
    # Iterate each cell to find whether to start BFS
    # Remember to memorize the visited cell by coordinates
    
    visited = set([])
    # visited is a bit tricky. It surely is updated when finish a examine a cell
    # It is also updated during counting size of a pond because when using
    # BFS or DFS to search a pond, a 
    
    sizes = set([])
    for i in range(m):
        for j in range(n):
            if (i, j) not in visited:
                visited.add((i, j))
                cell = Land[i][j]
                if cell == 0:
                    sizes.add(find_size_bfs(Land,m,n,(i,j),visited))
                    # also include visited to modify it along the bfs
    
    return sizes


# In[52]:

# Test
Land = [
    [0,2,1,0],
    [0,1,0,1],
    [1,1,0,1],
    [0,1,0,1]
]
print pond_size(Land)

