####				BASIC				####



import gym # the library that contains the environments we want to run the reinforcement agent in


env = gym.make('CartPole-v0') # create the environment. you can find more environments here: gym.openai.com/envs/
observation = env.reset() # initiate the environment + read the current observation of the environment
done = False # set enviroment-terminated boolean to be False right now

total_reward = 0
while not done: # while the environment-terminated boolean is still False
	env.render() # paint the graphics at the moment of running this line (since in a while loop, it will show the process of the episode)
	observation, reward, done, info = env.step(env.action_space.sample())
	#	the function step takes an action and returns the outputs from that action
	#	env.action_space.sample() chooses a random action between all the ones that are possible
	#	More info at: gym.openai.com/docs/

	total_reward += reward

print "\n\n\ttotal reward for this run is:", total_reward,"\n\n"
