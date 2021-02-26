# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
# 
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------

import numpy as np
from map import grid 
     
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
#goal = [4, 3]
cost = 1

delta = [[-1, 0], 
         [-1,-1],
         [ 0,-1],
         [ 1,-1],
         [ 1, 0],
         [ 1, 1],
         [ 0, 1],
         [-1, 1]]
delta_name = ['^', 'NW', '<', 'SW', 'v', 'SE', '>', 'NE']

def search(grid,init,goal,cost):
    rows = len(grid)
    cols =len(grid[0])
    no_grids = rows * cols
    heuristic = [[0 for col in range(len(grid[0]))] for row in range(len(grid))] 
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            heuristic[row][col] = heuristic[row][col] + np.sqrt(np.square((goal[0]+1)-(row+1)) + np.square((goal[1]+1)-(col+1)))
    #for row in range(len(grid)):
     #   for col in range(len(grid[0])):
      #      heuristic[row][col] = heuristic[row][col] + no_grids
       #     no_grids -= 1
    #print(heuristic)
    # in closed 0 being open and 1 being unchecked    
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    x = init[0]
    y = init[1]
    g = 0 
    h = heuristic[x][y]
    f = g + h 
    open = [[f, g, h, x, y]]
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
            x = next[3]
            y = next[4]
            g = next[1]
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
                            h2 = heuristic[x2][y2]
                            f2 = g2 + h2
                            open.append([f2, g2, h2, x2,y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
                            #print(open)  #Uncomment it to see the search path calculations
    print("Expansion sequence is like: \n")        
    for i in range(len(expand)):
        print(expand[i])
    if  found is True: 
        plan = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
        plan_grid = []
        x = goal[0]
        y = goal[1]
        plan[x][y] = '*'
        plan_grid = [[x, y]]
        while x != init[0] or y != init[1]:
            x2 = x - delta[action[x][y]][0]
            y2 = y - delta[action[x][y]][1]
            plan[x2][y2] = delta_name[action[x][y]]
            plan_grid.append([x2, y2])
            x = x2
            y = y2
        print("\nPlan is: \n")    
        for i in range(len(plan)):
            print(plan[i])
        final_plan = []
        for _ in range(len(plan_grid)):
            point = plan_grid.pop()
            final_plan.append(point)
        print("length of path generated: ",len(final_plan))
        print(final_plan)
    
    return open, final_plan

search(grid, init, goal, cost) 




