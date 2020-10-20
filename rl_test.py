import gym
from time import sleep
env = gym.make("CartPole-v0")


#initialize environment
obs = env.reset()

#obs is a four tuple representing an observation
#horizontal position
#velocity
#angle of the pole
#angular velocity

#what actions are possible
env.action_space
#Discrete(2)
#two discrete options, 0 and 1.
#0 is left; 1 is right

#env.render()

action = 1

obs, reward, done , info = env.step(action)


def basic_policy(obs):
    angle = obs[2] #angle of the pole, 0 = vertical
    return 0 if angle < 0 else 1

totals = []
for episode in range(500):
    episode_rewards = 0
    obs = env.reset()
    for step in range(1000):
        action = basic_policy(obs)
        obs, reward, done , info = env.step(action)
        env.render()
        sleep(0.03)
        episode_rewards += reward
        if done:
            env.reset()
            break
    totals.append(episode_rewards)

env.close()


        




