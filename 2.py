####				RANDOM SEARCH				####


import gym
import numpy as np # the library for scientific calculations in python (matrices, etc.)

NUM_OF_TESTS = 10000
NUM_OF_EPISODES = 200

env = gym.make('CartPole-v0')
observation = env.reset()

env._max_episode_steps = NUM_OF_EPISODES

def run_episode(env, parameters):  
	"""Runs the env for a certain amount of steps with the given parameters. Returns the reward obtained"""
	observation = env.reset()
	totalreward = 0
	done = False
	while not done:
		action = 0 if np.matmul(parameters, observation) < 0 else 1
		observation, reward, done, info = env.step(action)
		totalreward += reward
	return totalreward 

# keeping track of the best parameters
bestparams = None  
bestreward = 0  

# running tests to find the paramaters that give the highest reward, to keep it. (probably) that's a good one
for _ in xrange(NUM_OF_TESTS):
	# create random new parameters that would match the shape of observation
	parameters = np.random.rand(4) * 2 - 1 
	# find the reward of this set of parameters and if it's better the ones before, update the values
	reward = run_episode(env, parameters)
	if reward > bestreward:
        	bestreward = reward
        	bestparams = parameters
        	# considered solved if the agent lasts the max number of episodes
		if reward == NUM_OF_EPISODES:
			break

# uncomment to save a video of the episode that is going to happen
# env = gym.wrappers.Monitor(env, '.', Force=True)
observation = env.reset()
done = False
rewardAll = 0
# show a run using the best set of parameters
while not done:
	env.render()
	action = 0 if np.matmul(parameters, observation) < 0 else 1
	observation, reward, done, info = env.step(action)
	rewardAll += reward
