##################################################################################################
# 1. Till now I have only implemented for static map without other agents. How to generalize it to 
# dynamic local map? 
# 2. Also one small thing: Sensing area should be circular with radius equal to sensing range. 
# Currently I am using square for sensing area not circular. 
################################################################################################
from map import grid

c_pose = [3,4] # later use c_pose instead of init
sense = 7    # Define the sensing range here 
obs = [[1 for col in range(15)] for row in range(15)]
#print(obs)
##################################################################################
# Trial: 5
#shift_x = sense - c_pose[0]
#shift_y = sense - c_pose[1]
#sen_grid = []
#for row in range(len(grid)):
 #   for col in range(len(grid[0])):
  #      if abs(c_pose[0]-row) <= sense and abs(c_pose[1]-col) <= sense:
   #         sen_grid.append([row,col])
#print(sen_grid)
#print(sen_grid[0][1]) 
#for i in range(len(sen_grid)):
 #   obs[sen_grid[i][0]+shift_x][sen_grid[i][1]+shift_y] = grid[sen_grid[i][0]][sen_grid[i][1]]
#obs[sense][sense] = 1
#print(obs)    
#######################################################################################################
#Trial: 6
shift_x = sense - c_pose[0]
shift_y = sense - c_pose[1]
sen_grid = []
a = []
for i in range(2*sense+1):
    a.append((-sense+i))
#print(a)
for i in range(2*sense+1):
    for j in range(2*sense+1):
        x = c_pose[0]
        y = c_pose[1]
        if x+a[i]>=0 and y+a[j]>=0 and x+a[i]<=len(grid)-1 and y+a[j]<=len(grid[0])-1:
            sen_grid.append([(x+a[i]), (y+a[j])])                   
#print(sen_grid) 
for i in range(len(sen_grid)):
    obs[sen_grid[i][0]+shift_x][sen_grid[i][1]+shift_y] = grid[sen_grid[i][0]][sen_grid[i][1]]
obs[sense][sense] = 1
print(obs)    