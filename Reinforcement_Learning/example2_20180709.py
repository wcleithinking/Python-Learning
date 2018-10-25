# _*_ coding: utf-8 _*_
#! /usr/bin/python

# Import the Modules
from maze_env import Maze
from RL_brain import QLearningTable

# Update the QLearningTable
def update():
    for episode in range(100):
        observation = env.reset()
        
        while True:
            env.render()

            action = RL.choose_action(str(observation))

            observation_next, reward, done = env.step(action)

            RL.learn(str(observation),action,reward,str(observation_next))

            observation = observation_next

            if done:
                break
    print('game over')
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100,update)
    env.mainloop()
