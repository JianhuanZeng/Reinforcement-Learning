def reward_generate(p):
    return np.random.binomial(1, p)

def epsl_greedy(T,n,epsilon,probabilities):
    """
    T: the toto number of trails
    n: the total number of arms
    probabilities: probability of success of each arm i
    """

    # initialize
    arm_selected = [] # arm selected over n arms
    numbers_of_selections = [0] * n # Ti
    avg_of_rewards= [0] * n
    sums_of_rewards = [0] * n # sum of reward each i
    total_reward = 0 # total reward at time t
    avg_rewards = [] # average reward over time T

    for t in range(T):
        """
        for the second algorithm, add "epslon=1/t" below
        """
        #epsilon=1/(t+1)
        # picking a arm
        if np.random.rand() > epsilon:
            ai=np.argmax(avg_of_rewards)
        else:
            ai=np.random.choice(5)

        # updating data
        arm_selected.append(ai)
        numbers_of_selections[ai] = numbers_of_selections[ai] + 1
        reward = reward_generate(probabilities[ai])
        sums_of_rewards[ai] = sums_of_rewards[ai] + reward
        avg_of_rewards[ai]=sums_of_rewards[ai]/numbers_of_selections[ai]
        total_reward = total_reward + reward
        avg_rewards.append(total_reward/(t+1))
    return avg_rewards

T = 1000 # the number of times of trails
n = 5 # the total number of arms
epslon=0.1
probabilities=[0.1, 0.5, 0.8, 0.7, 0.65]
