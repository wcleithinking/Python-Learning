# _*_ coding: utf-8 _*_
#! usr/bin/python

# Import the Modules
from __future__ import print_function
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

# Set the Initial Values
N_states = 50    # the width of the one dimensional word
Actions = ['left','right']  # the available actions
epsilon = 0.8   # the greedy number
alpha = 0.1 # learning rate
gamma = 0.9 # decay of the rewards
max_episode = 50
fresh_time = 0.001

# Build the Q-Table
def build_q_table(n_states, actions):
    table = pd.DataFrame(
            np.zeros((n_states,len(actions))),
            columns = actions,
            )
    return table

# Initial Q_Table
"""
    left    right
0   0.0     0.0
1   0.0     0.0
2   0.0     0.0
3   0.0     0.0
4   0.0     0.0
5   0.0     0.0
... 0.0     0.0
"""

# Choose the Action
def choose_action(state, q_table):
    state_actions = q_table.iloc[state,:]
    if (np.random.uniform() > epsilon) or (state_actions.all() == 0):   # not greedy or not explored
        action_name = np.random.choice(Actions)
    else:
        action_name = state_actions.idxmax()
    return action_name

# Get the Environment Feedback
def get_env_feedback(S,A):
    # rules
    if A == 'right':
        if S == N_states - 2:
            S_next = 'terminal'
            R = 1
        else:
            S_next = S+1
            R = 0
    else:
        R = 0
        if S == 0:
            S_next = S
        else:
            S_next = S-1
    return S_next, R

# Update the Environment
def update_env(S, episode, step_counter):
    env_list = ['-']*(N_states-1) + ['T']   # '-----T' our environment
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' %(episode+1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(1)
        print('\r                                                              ', end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(fresh_time)

# Reinforcement Learning Algorithm
def rl():
    q_table = build_q_table(N_states,Actions)
    episode_log = []
    step_log = []
    for episode in range(max_episode):
        step_counter = 0
        S = 0
        is_terminated = False
        update_env(S, episode, step_counter)
        while not is_terminated:
            A = choose_action(S,q_table)
            S_next,R = get_env_feedback(S,A)
            q_predict = q_table.loc[S,A]
            if S_next != 'terminal':
                q_target = R + gamma*q_table.iloc[S_next,:].max()
            else:
                q_target = R
                is_terminated = True
            q_table.loc[S,A] += alpha*( q_target - q_predict )
            S = S_next
            update_env(S, episode, step_counter+1)
            step_counter +=1
        episode_log.append(episode+1)
        step_log.append(step_counter) 
    return q_table, episode_log, step_log

# Main Program
if __name__ == "__main__":
    q_table,episode_log,step_log = rl()
    print('\r\nQ-table:\n')
    print(q_table)
    plt.figure(1)
    plt.plot(episode_log, step_log,'b-*')
    plt.xlim(1, max_episode)
    plt.title('Reinforcement Learning Results')
    plt.xlabel('Episode')
    plt.ylabel('Total_Step')
    plt.show()
