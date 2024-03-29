# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 16:12:01 2020
Udacity AI for Robotics course: problem set 1
@author: Joy
"""

# The function localize takes the following arguments:
#
# colors:
#        2D list, each entry either 'R' (for red cell) or 'G' (for green cell)
#
# measurements:
#        list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:
#        list of actions taken by the robot, each entry of the form [dy,dx],
#        where dx refers to the change in the x-direction (positive meaning
#        movement to the right) and dy refers to the change in the y-direction
#        (positive meaning movement downward)
#        NOTE: the *first* coordinate is change in y; the *second* coordinate is
#              change in x
#
# sensor_right:
#        float between 0 and 1, giving the probability that any given
#        measurement is correct; the probability that the measurement is
#        incorrect is 1-sensor_right
#
# p_move:
#        float between 0 and 1, giving the probability that any given movement
#        command takes place; the probability that the movement command fails
#        (and the robot remains still) is 1-p_move; the robot will NOT overshoot
#        its destination in this exercise
#
# The function should RETURN (not just show or print) a 2D list (of the same
# dimensions as colors) that gives the probabilities that the robot occupies
# each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform
# probability of being in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up

def localize(colors,measurements,motions,sensor_right,p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    
    for i in range(len(measurements)):
        p = move(p, motions[i], p_move)
        p = sense(p, measurements[i], colors, sensor_right)
        
    return p

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print('[' + ',\n '.join(rows) + ']')
    
#############################################################
# For the following test case, your output should be 
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)

def sense(p_clone, Z, colors, sensor_right):
    q = [[0.0 for i in range(len(p_clone[0]))] for j in range(len(p_clone))]
    s = 0
    for i in range(len(p_clone)):
        for j in range(len(p_clone[0])):
            hit = (Z == colors[i][j])
            q[i][j] = (p_clone[i][j] * (hit * sensor_right + (1-hit) * (1-sensor_right)))
            s += q[i][j]        
    for k in range(len(p_clone)):
        for l in range(len(p_clone[0])):
            q[k][l] = q[k][l] / s
    return q         

def move(p_clone, U, p_move):
    q_clone = [[0.0 for i in range(len(p_clone[0]))] for j in range(len(p_clone))]
    for i in range(len(p_clone)):
        for j in range(len(p_clone[0])):
            q_clone[i][j] = p_move * p_clone[(i - U[0]) % len(p_clone)][(j - U[1]) % len(p_clone[0])]
            q_clone[i][j] = q_clone[i][j] + (1 - p_move) * p_clone[i][j]
            
    return q_clone
    

colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
if len(measurements) != len(motions):
    raise ValueError("Length of measurements and motions are not equal.")
p = localize(colors,measurements,motions,sensor_right = 0.7, p_move = 0.8)
show(p) # displays your answer

