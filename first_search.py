# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space
from map import grid

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
#goal = [13, 3]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # in closed 0 being open and 1 being unchecked    
    #closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid[1]))]
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1
    #expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid[1]))]
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    #action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid[1]))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    x = init[0]
    y = init[1]
    g = 0
    open = [[g, x, y]]
    count = 0
    found = False # flag that is set when search is complete
    resign = False # flag set if we can't find expand
     
    while found is False and resign is False:
        # Check if we still have elements in open list
        if len(open) == 0:
            resign = True
            print("Fail, Search terminated without success")
        else:
            # remove node from list
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            expand[x][y] = count
            count += 1
            # check if we are done
            if x == goal[0] and y == goal[1]:
                found = True
                print(next)
                print("Search successful")
            else:
                # expand winning element and add to new open list
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
                            #print(open)  #Uncomment it to see the search path calculations
    print("Expansion sequence is like: \n")        
    for i in range(len(expand)):
        print(expand[i])
    if  found is True: 
        plan = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
        x = goal[0]
        y = goal[1]
        plan[x][y] = '*'
        plan_grid = [[x, y]]
        while x != init[0] or y != init[1]:
            x2 = x - delta[action[x][y]][0]
            y2 = y - delta[action[x][y]][1]
            plan[x2][y2] = delta_name[action[x][y]]
            plan_grid.append([x2,y2])
            x = x2
            y = y2
        print("Plan is: \n")    
        for i in range(len(plan)):
            print(plan[i])
        print(len(plan_grid))

    return open

search(grid, init, goal, cost) 
