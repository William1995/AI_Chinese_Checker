#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
from collections import Counter
import copy

def initialize(board):
    start_board = []
    with open("data1/initial.txt") as file:
        for line in file.readlines():
            line = line.strip('\n')
            start_board.append(eval(line))
    start_board.remove(start_board[0])
    board = start_board
    print board
    return board

def end_board(board):
    end_board = [(-4,-4),(-3,-4),(-2,-4),(-1,-4),(0,-4),
                 (-4,-3),(-3,-3),(-2,-3),(-1,-3),
                 (-4,-2),(-3,-2),(-2,-2),
                 (-4,-1),(-3,-1),
                 (-4,0)]
    board = end_board
    return board

def check_end_state(board1,board2):
    if board1 in board2:
        return 0
    else:
        return 1

def compute_distance(checker,board2):
    D = 0
    D = math.sqrt((checker[0]-board2[0])**2 + (checker[1]-board2[1])**2)
    return D

def origin_d(start_board,end_state):
    l = 0
    l = len(start_board)
    temp = []
    for i in range(0,l):
        D = i+1
        temp.append(D)
    return temp

def build(world_board):
    world = [(4,-8),
             (3,-7),(4,-7),
             (2,-6),(3,-6),(4,-6),
             (1,-5),(2,-5),(3,-5),(4,-5),
             (-4,-4),(-3,-4),(-2,-4),(-1,-4),(0,-4),(1,-4),(2,-4),(3,-4),(4,-4),(5,-4),(6,-4),(7,-4),(8,-4),
             (-4,-3),(-3,-3),(-2,-3),(-1,-3),(0,-3),(1,-3),(2,-3),(3,-3),(4,-3),(5,-3),(6,-3),(7,-3),
             (-4,-2),(-3,-2),(-2,-2),(-1,-2),(0,-2),(1,-2),(2,-2),(3,-2),(4,-2),(5,-2),(6,-2),
             (-4,-1),(-3,-1),(-2,-1),(-1,-1),(0,-1),(1,-1),(2,-1),(3,-1),(4,-1),(5,-1),
             (-4,0),(-3,0),(-2,0),(-1,0),(0,0),(1,0),(2,0),(3,0),(4,0),
             (-5,1),(-4,1),(-3,1),(-2,1),(-1,1),(0,1),(1,1),(2,1),(3,1),(4,1),
             (-6,2),(-5,2),(-4,2),(-3,2),(-2,2),(-1,2),(0,2),(1,2),(2,2),(3,2),(4,2),
             (-7,3),(-6,3),(-5,3),(-4,3),(-3,3),(-2,3),(-1,3),(0,3),(1,3),(2,3),(3,3),(4,3),
             (-8,4),(-7,4),(-6,4),(-5,4),(-4,4),(-3,4),(-2,4),(-1,4),(0,4),(1,4),(2,4),(3,4),(4,4),
             (-4,5),(-3,5),(-2,5),(-1,5),
             (-4,6),(-3,6),(-2,6),
             (-4,7),(-3,7),
             (-4,8)]
    board = world
    return board

def caculate_slide(str,end):
    k = 0
    if (end[0] - str[0]) != 0:
        k = (end[1] - str[1]) / float(end[0] - str[0])
    else:
        k = 1000
    return k

#------main------#

#initialize#
board = []
end_state = []
origin_distance = []
world = []
board = initialize(board)
end_state = end_board(end_state)
origin_distance = origin_d(board,end_state)
world = build(world)

check = 1
cost = []
temp_board = []
next_move_checker = 0
moved_checker = 100
count_move = 0
cost = copy.deepcopy(origin_distance)
target = end_state[0]
f = 0
L = 0
completed = []
haved_done = []
continuous = 0

#core#
while check != 0:
    check = check_end_state(board,end_state)
    temp_board = copy.deepcopy(board)
    i =0
    L = len(board)
    continuous = 0
    
    if check == 1:
        #選出距離最小的移動#
        next_move_checker = cost.index(min(cost))
        temp_d = 0
        i = next_move_checker
        k = 0
        
        #選擇方向#
        k = caculate_slide(board[i],target)
        
        
        #檢查是否可以移動#
        if temp_board[i] not in haved_done:
            #平行#
            if k == 0:
                #左邊跳#
                if (temp_board[i][0]-1,temp_board[i][1]) in board and (temp_board[i][0]-2,temp_board[i][1]) not in board and (temp_board[i][0]-2,temp_board[i][1]) in world:
                    temp_d = compute_distance(temp_board[i],(temp_board[i][0]-2,temp_board[i][1]))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0]-2,temp_board[i][1])
                    continuous = 2
                    if moved_checker != next_move_checker:
                        count_move = count_move +1
                
                #右邊跳#
                elif (temp_board[i][0]+1,temp_board[i][1]) in board and (temp_board[i][0]+2,temp_board[i][1]) not in board and (temp_board[i][0]+2,temp_board[i][1]) in world:
                    temp_d = compute_distance(temp_board[i],(temp_board[i][0]+2,temp_board[i][1]))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0]+2,board[i][1])
                    continuous = 2
                    if moved_checker != next_move_checker:
                        count_move = count_move +1
                
                #左邊走#
                elif (temp_board[i][0]-1,temp_board[i][1]) not in board and (temp_board[i][0]-1,temp_board[i][1]) in world:
                    temp_d = compute_distance(temp_board[i],(temp_board[i][0]-1,temp_board[i][1]))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0]-1,temp_board[i][1])
                    continuous = 1
                    count_move = count_move +1
                
                
                #右邊走#
                elif (temp_board[i][0]+1,temp_board[i][1]) not in board and (temp_board[i][0]+1,temp_board[i][1]) in world:
                    temp_d = compute_distance(temp_board[i],(temp_board[i][0]+1,temp_board[i][1]))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0]+1,temp_board[i][1])
                    continuous = 1
                    count_move = count_move +1
                
        
                #不能動#
                else:
                    cost[i] = cost[i] + 100
                    continuous = 0
        
            #垂直#
            elif k == 1000:
                #左下跳#
                if (temp_board[i][0],temp_board[i][1]-1) in board and (temp_board[i][0],temp_board[i][1]-2) not in board and (temp_board[i][0],temp_board[i][1]-2) in world:
                    temp_d = compute_distance(board[i],(temp_board[i][0],temp_board [i][1]-2))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0],temp_board[i][1]-2)
                    continuous = 2
                    if moved_checker != next_move_checker:
                        count_move = count_move +1
                
                #左下走#
                elif (temp_board[i][0],temp_board[i][1]-1) not in board and (temp_board[i][0],temp_board[i][1]-1) in world:
                    temp_d = compute_distance(temp_board[i],(temp_board[i][0],temp_board[i][1]-1))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0],temp_board[i][1]-1)
                    continuous = 1
                    count_move = count_move +1
                
                
                #右上跳#
                elif (temp_board[i][0],temp_board[i][1]+1) in board and (temp_board[i][0],temp_board[i][1]+2) not in board and (temp_board[i][0],temp_board[i][1]+2) in world:
                    temp_d = compute_distance(board[i],(temp_board[i][0],temp_board [i][1]+2))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0],temp_board[i][1]+2)
                    continuous = 2
                    if moved_checker != next_move_checker:
                        count_move = count_move +1
                
                #右上走#
                elif (temp_board[i][0],temp_board[i][1]+1) not in board and (temp_board[i][0],temp_board[i][1]+1) in world:
                    temp_d = compute_distance(temp_board[i],(temp_board[i][0],temp_board[i][1]+1))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0],temp_board[i][1]+1)
                    continuous = 1
                    count_move = count_move +1
                
                
                
                #不能動#
                else:
                    cost[i] = cost[i] + 100
                    continuous = 0
            
            #左邊#
            elif k < 0:
                
                #左上跳#
                if (temp_board[i][0]-1,temp_board[i][1]+1) in board and (temp_board[i][0]-2,temp_board[i][1]+2) not in board and (temp_board[i][0]-2,temp_board[i][1]+2) in world:
                    temp_d = compute_distance(temp_board[i],(temp_board[i][0]-2,temp_board[i][1]+2))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0]-2,temp_board[i][1]+2)
                    continuous = 2
                    if moved_checker != next_move_checker:
                        count_move = count_move +1
            
                #左上走#
                elif (temp_board[i][0]-1,temp_board[i][1]+1) not in board and (temp_board[i][0]-1,temp_board[i][1]+1) in world:
                    temp_d = compute_distance(temp_board[i],(temp_board[i][0]-1,temp_board[i][1]+1))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0]-1,temp_board[i][1]+1)
                    continuous = 1
                    count_move = count_move +1
                

                #左邊跳#
                elif (temp_board[i][0]-1,temp_board[i][1]) in board and (temp_board[i][0]-2,temp_board[i][1]) not in board and (temp_board[i][0]-2,temp_board[i][1]) in world:
                    temp_d = compute_distance(temp_board[i],(temp_board[i][0]-2,temp_board[i][1]))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0]-2,temp_board[i][1])
                    continuous = 2
                    if moved_checker != next_move_checker:
                        count_move = count_move +1

                #左邊走#
                elif (temp_board[i][0]-1,temp_board[i][1]) not in board and (temp_board[i][0]-1,temp_board[i][1]) in world:
                    temp_d = compute_distance(temp_board[i],(temp_board[i][0]-1,temp_board[i][1]))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0]-1,temp_board[i][1])
                    continuous = 1
                    count_move = count_move +1
                
                
                #右下跳#
                elif (temp_board[i][0]+1,temp_board[i][1]-1) in board and (temp_board[i][0]+2,temp_board[i][1]-2) not in board and (temp_board[i][0]+2,temp_board[i][1]-2) in world:
                    temp_d = compute_distance(board[i],(temp_board[i][0]+2,temp_board [i][1]-2))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0]+2,temp_board[i][1]-2)
                    continuous = 2
                    if moved_checker != next_move_checker:
                        count_move = count_move +1
                
                #右下走#
                elif (temp_board[i][0]+1,temp_board[i][1]-1) not in board and (temp_board[i][0]+1,temp_board[i][1]-1) in world:
                    temp_d = compute_distance(temp_board[i],(temp_board[i][0]+1,temp_board[i][1]-1))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0]+1,temp_board[i][1]-1)
                    continuous = 1
                    count_move = count_move +1
                

                #不能動#
                else:
                    cost[i] = cost[i] + 100
                    continuous = 0

            #右邊#
            elif k > 0:
                #左下跳#
                if (temp_board[i][0],temp_board[i][1]-1) in board and (temp_board[i][0],temp_board[i][1]-2) not in board and (temp_board[i][0],temp_board[i][1]-2) in world:
                    temp_d = compute_distance(board[i],(temp_board[i][0],temp_board [i][1]-2))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0],temp_board[i][1]-2)
                    continuous = 2
                    if moved_checker != next_move_checker:
                        count_move = count_move +1
                
                #左下走#
                elif (temp_board[i][0],temp_board[i][1]-1) not in board and (temp_board[i][0],temp_board[i][1]-1) in world:
                    temp_d = compute_distance(temp_board[i],(temp_board[i][0],temp_board[i][1]-1))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0],temp_board[i][1]-1)
                    continuous = 1
                    count_move = count_move +1
                
                
                #右上跳#
                elif (temp_board[i][0],temp_board[i][1]+1) in board and (temp_board[i][0],temp_board[i][1]+2) not in board and (temp_board[i][0],temp_board[i][1]+2) in world:
                    temp_d = compute_distance(board[i],(temp_board[i][0],temp_board [i][1]+2))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0],temp_board[i][1]+2)
                    continuous = 2
                    if moved_checker != next_move_checker:
                        count_move = count_move +1
                
                #右上走#
                elif (temp_board[i][0],temp_board[i][1]+1) not in board and (temp_board[i][0],temp_board[i][1]+1) in world:
                    temp_d = compute_distance(temp_board[i],(temp_board[i][0],temp_board[i][1]+1))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0],temp_board[i][1]+1)
                    continuous = 1
                    count_move = count_move +1
                

                #右邊跳#
                elif (temp_board[i][0]+1,temp_board[i][1]) in board and (temp_board[i][0]+2,temp_board[i][1]) not in board and (temp_board[i][0]+2,temp_board[i][1]) in world:
                    temp_d = compute_distance(temp_board[i],(temp_board[i][0]+2,temp_board[i][1]))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0]+2,board[i][1])
                    continuous = 2
                    if moved_checker != next_move_checker:
                        count_move = count_move +1

                #右邊走#
                elif (temp_board[i][0]+1,temp_board[i][1]) not in board and (temp_board[i][0]+1,temp_board[i][1]) in world:
                    temp_d = compute_distance(temp_board[i],(temp_board[i][0]+1,temp_board[i][1]))
                    cost[i] = cost[i] + temp_d
                    temp_board[i] = (temp_board[i][0]+1,temp_board[i][1])
                    continuous = 1
                    count_move = count_move +1
                


                #不能動#
                else:
                    cost[i] = cost[i] + 100
                    continuous = 0


            #if(moved_checker!=next_move_checker):
            if continuous != 0:
                print '\n' + str(board[next_move_checker]) + ';' + str(temp_board[next_move_checker]) + ';'
            
            #else:
            #print str(temp_board[next_move_checker]) + ';'
            #改變棋盤到新狀態#
            moved_checker = next_move_checker
            board[next_move_checker] = temp_board[next_move_checker]

            #確認是否有達到目標#
            if temp_board[i] == target:
                f = f + 1
                if f == L:
                    check = 0
                    print count_move
                    print board
                    #print haved_done
                else:
                    haved_done.append(temp_board[i])
                    completed.append(next_move_checker)
                    #print board
                    cost[i] = cost[i] + 10000
                    target = end_state[f]




