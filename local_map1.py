#############################################################################################
# 1. It is working but I am checking for all grids which are in sensing range to find sen_grid.
# This is not good because for big map it can take time to find this list. How to make it more efficient?
# 2. Till now I have only implemented for static map without other agents. How to generalize it to 
# dynamic local map? 
################################################################################################
from map import grid

c_pose = [1,2] # later use c_pose instead of init
sense = 7  # Set the sensing range here
obs = [[1 for col in range(15)] for row in range(15)]
#print(obs)
########################################################################################
#Trial: 4
#shift_x = 2 - c_pose[0]
#shift_y = 2 - c_pose[1]
#for row in range(len(obs)):
 #   for col in range(len(obs[0])):
  #      if (row+shift_x)>=0 and (col+shift_y)>=0 and (col+shift_y)<len(obs[0]) and (row+shift_x)<len(obs):
   #         obs[row+shift_x][col+shift_y] = grid[row][col]
    #        print(obs)
     #   else:
      #      obs[(row+shift_x)%(len(obs))][(col+shift_y)%(len(obs[0]))]=1    
       #     print(obs)
#obs[sense][sense] = 1
#print(obs)
###########################################################################################
# Trial: 5
shift_x = sense - c_pose[0]
shift_y = sense - c_pose[1]
sen_grid = []
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if abs(c_pose[0]-row) <= sense and abs(c_pose[1]-col) <= sense:
            sen_grid.append([row,col])
#print(sen_grid)
#print(sen_grid[0][1]) 
for i in range(len(sen_grid)):
    obs[sen_grid[i][0]+shift_x][sen_grid[i][1]+shift_y] = grid[sen_grid[i][0]][sen_grid[i][1]]
obs[sense][sense] = 1
print(obs)    
