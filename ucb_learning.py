# Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import math


def reward_generate(p):
    return np.random.binomial(1, p)

def upper_bound(average_reward, alpha,t,T):
    return average_reward + math.sqrt(alpha/2 * math.log(t + 1)/T)

def ucb(T,n,alpha,probabilities):
    """
    T: the toto number of trails
    n: the total number of arms
    probabilities: probability of success of each arm i
    """

    # initialize
    arm_selected = [] # arm_selected
    numbers_of_selections = [0] * n # Ti
    sums_of_rewards = [0] * n # sum of reward each i
    total_reward = 0 # total reward at time t
    avg_rewards = [] # average reward over time T

    for t in range(T):
        ai = 0
        max_upper_bound = 0

        #picking a arm
        for i in range(n):
            if (numbers_of_selections[i] > 0):
                average_reward_i = sums_of_rewards[i] / numbers_of_selections[i]
                upper_bound_i = upper_bound(average_reward_i,alpha,t,numbers_of_selections[i])
            else:
                # value 10 for unexploited arms
                upper_bound_i = 10

            # choosing the arm i with maximun upper_bound
            if upper_bound_i > max_upper_bound:
                max_upper_bound = upper_bound_i
                ai = i

        # updating data
        arm_selected.append(ai)
        numbers_of_selections[ai] = numbers_of_selections[ai] + 1
        reward = reward_generate(probabilities[ai])
        sums_of_rewards[ai] = sums_of_rewards[ai] + reward
        total_reward = total_reward + reward
        avg_rewards.append(total_reward/(t+1))
    return avg_rewards

# Implementing UCB
T = 1000 # the number of times of trails
n = 5 # the total number of arms
alpha=2
probabilities=[0.1, 0.5, 0.8, 0.7, 0.65]
