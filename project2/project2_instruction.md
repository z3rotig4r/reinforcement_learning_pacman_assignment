# CSE 17182 Artificial Intelligence, Fall 2025: Project \#2 - Reinforcement Learning

## 1\. Project Overview

  * [cite_start]In this project, you will implement Value Iteration and Q-learning. [cite: 6]
  * [cite_start]You will test your agents first on Gridworld, then apply them to a simulated robot controller (Crawler) and Pacman. [cite: 7]
  * [cite_start]You will get six different tasks within this project. [cite: 9]
  * [cite_start]This assignment reuses UC Berkeley's Pacman AI project ([https://ai.berkeley.edu/](https://ai.berkeley.edu/)), but with minimum adjustments for CAU's CSE 17182. [cite: 10]

## 2\. Environment

  * [cite_start]Projects in this class require Python 3.6+. [cite: 13]
  * [cite_start]For the grading, I will use vanilla Python 3.9 in a conda environment. [cite: 14]
  * [cite_start]If you want the same setup, install conda and run the following commands: [cite: 15]

<!-- end list -->

```bash
conda create -n pacman python-3.9 -y
conda activate pacman
python --version # should show 3.9.x
```

[cite_start][cite: 16, 17, 18]

## 3\. Submission Deliverable & Deadline

  * [cite_start]**Deadline:** Dec 12 (Fri) 23:59 (through the e-class system). [cite: 21]
  * [cite_start]Within the code files from the given zip archive (`project2.zip`), you are allowed to edit **ONLY** the following three files (please do not change the filenames): [cite: 22, 23]
      * [cite_start]`valueIterationAgents.py` [cite: 24]
      * [cite_start]`qlearningAgents.py` [cite: 25]
      * [cite_start]`analysis.py` [cite: 26]
  * [cite_start]As a submission, you need to make the three files compressed and submit as **ONE** zip file with a filename `submission.zip`. [cite: 27]
  * [cite_start]If you violate this deliverable rule, huge penalty will be applied to your score. [cite: 28]

## 4\. Auto-grading

You can try to grade your answers on your machine. [cite_start]This can be done using the following commands: [cite: 31, 32, 33]

  * Run on all questions:
    ```bash
    python autograder.py
    ```
    [cite_start][cite: 33]
  * Run on a particular question:
    ```bash
    python autograder.py -q q2
    ```
    [cite_start][cite: 34]

## 5\. Starter: Try the Gridworld MDP

  * [cite_start]The given files provide you to run Gridworld in manual control mode (using the arrow keys): [cite: 40]
    ```bash
    python gridworld.py -m
    ```
    [cite_start][cite: 40]
  * [cite_start]In this project, you will build your own agents (with Value Iteration or Q-learning). [cite: 41]
  * [cite_start]After the implementation, you can test your agents as follows (the following code will not work until you implement those agents): [cite: 42]
      * Value Iteration (Q1):
        ```bash
        python gridworld.py -a value
        ```
        [cite_start][cite: 43]
      * Q-learning (Q3):
        ```bash
        python gridworld.py -a q
        ```
        [cite_start][cite: 44]
  * You can control many aspects of the simulation. [cite_start]A full list of options is available by running: [cite: 45]
    ```bash
    python gridworld.py -h
    ```
    [cite_start][cite: 46]

## 6\. Other information

[cite_start]Within the zip archive, you may want to read the following five files of code: [cite: 51]

  * [cite_start]`mdp.py`: Defines methods on general MDPs. [cite: 51]
  * [cite_start]`learningAgents.py`: Defines the base classes `ValueEstimationAgent` and `QLearningAgent`, which your agents will extend. [cite: 52]
  * [cite_start]`util.py`: Utilities, including `util.Counter`, which is particularly useful for Q-learners. [cite: 53]
  * [cite_start]`gridworld.py`: The Gridworld implementation. [cite: 54]
  * `featureExtractors.py`: Classes for extracting features on (state, action) pairs. [cite_start]Used for the approximate Q-learning agent (in `qlearningAgents.py`). [cite: 55, 56]
  * [cite_start]You can neglect other supporting files (e.g., `environment.py`). [cite: 57]

-----

## Q1 (5 pts). Value Iteration

[cite_start]**Update this file:** `valueIterationAgents.py` [cite: 58, 59]

[cite_start]Recall the value iteration state update equation: [cite: 60]

$$V_{k+1}(s)\leftarrow \max_{a}\sum_{s^{\prime}}T(s,a,s^{\prime})[R(s,a,s^{\prime})+\gamma V_{k}(s^{\prime})]$$
[cite_start][cite: 61]

  * [cite_start]Write a value iteration agent in `ValueIterationAgent`, which has been partially specified for you in `valueIterationAgents.py`. [cite: 62]
  * [cite_start]`ValueIterationAgent` takes an MDP on construction and runs value iteration for the specified number of iterations (= argument `iterations`) before the constructor returns. [cite: 63]
  * [cite_start]Value iteration computes k-step estimates of the optimal values, $V_{k}$. [cite: 64]
  * [cite_start]In addition to `runValueIteration`, implement the following methods for `ValueIterationAgent` using $V_{k}$: [cite: 65]
      * [cite_start]`computeActionFromValues(state)`: computes the best action according to the value function given by `self.values`. [cite: 67]
      * [cite_start]`computeQValueFromValues(state, action)`: returns the Q-value of the (state, action) pair given by the value function given by `self.values`. [cite: 68]

**Notes:**

  * [cite_start]A policy synthesized from values of depth $k$ (which reflect the next $k$ rewards) will actually reflect the next $k+1$ rewards (i.e., you return $\pi_{k+1}$). [cite: 72]
  * [cite_start]Similarly, the Q-values will also reflect one more reward than the values (i.e., you return $Q_{k+1}$). [cite: 73]
  * [cite_start]As a computed action, you should return the synthesized policy $\pi_{k+1}$. [cite: 74]
  * [cite_start]**Hint:** You may optionally use the `util.Counter` class in `util.py`, which is a dictionary with a default value of zero. [cite: 75] [cite_start]However, be careful with `argmax`: the actual `argmax` you want may be a key not in the counter\! [cite: 76]
  * [cite_start]**Note:** Make sure to handle the case when a state has no available actions in an MDP. [cite: 77]

**Test your implementation:**
[cite_start]The following command loads your `ValueIterationAgent`, which will compute a policy for 100 iteration updates (option `-i`) and execute it 10 times (option `-k`). [cite: 79]

```bash
python gridworld.py -a value -i 100 -k 10
```

[cite_start][cite: 80]

[cite_start]On the default grid, running value iteration for 5 iterations should give you this output: [cite: 81]

```bash
python gridworld.py -a value -i 5
```

[cite_start][cite: 82]

**Expected Output Values:**

  * [cite_start]0.51 [cite: 83]
  * [cite_start]0.72 [cite: 84]
  * [cite_start]0.84 [cite: 85]
  * [cite_start]1.00 [cite: 86]
  * [cite_start]0.27 [cite: 87]
  * [cite_start]0.55 [cite: 88]
  * [cite_start]-1.00 [cite: 89]
  * [cite_start]0.00 [cite: 90]
  * [cite_start]0.22 [cite: 91]
  * [cite_start]0.37 [cite: 92]
  * [cite_start]0.13 [cite: 92]

**Grading:**

  * Your value iteration agent will be graded on a new grid. [cite_start]We will check your values, Q-values, and policies after fixed numbers of iterations and at convergence (e.g., after 100 iterations). [cite: 95, 97, 98]
  * [cite_start]You can run the autograder to check your points: [cite: 99]
    ```bash
    python autograder.py -q q1
    ```
    [cite_start][cite: 100]

-----

## Q2 (5 pts). Policies

[cite_start]**Update this file:** `analysis.py` [cite: 103, 104]

Consider the `DiscountGrid` layout. [cite_start]This grid has two terminal states with positive payoff (in the middle row), a close exit with payoff +1 and a distant exit with payoff +10. [cite: 106] [cite_start]The bottom row of the grid consists of terminal states with negative payoff (shown in red); each state in this "cliff" region has payoff -10. [cite: 107, 108] [cite_start]The starting state is the yellow square. [cite: 108]

We distinguish between two types of paths:

1.  [cite_start]Paths that "risk the cliff" and travel near the bottom row of the grid; these paths are shorter but risk earning a large negative payoff. [cite: 109]
2.  Paths that "avoid the cliff" and travel along the top edge of the grid. [cite_start]These paths are longer but are less likely to incur huge negative payoffs. [cite: 109, 110]

[cite_start]In this question, you will choose settings of the discount, noise, and living reward parameters for this MDP to produce optimal policies of several different types. [cite: 116] [cite_start]Your setting of the parameter values for each part should have the property that, if your agent followed its optimal policy without being subject to any noise, it would exhibit the given behavior. [cite: 117] [cite_start]If a particular behavior is not achieved for any setting of the parameters, assert that the policy is impossible by returning the string `'NOT POSSIBLE'`. [cite: 118]

[cite_start]**Here are the optimal policy types you should attempt to produce:** [cite: 121]

  * [cite_start]**2a)** Prefer the close exit (+1), risking the cliff (-10) [cite: 122]
  * [cite_start]**2b)** Prefer the close exit (+1), but avoiding the cliff (-10) [cite: 123]
  * [cite_start]**2c)** Prefer the distant exit (+10), risking the cliff (-10) [cite: 124]
  * [cite_start]**2d)** Prefer the distant exit (+10), avoiding the cliff (-10) [cite: 125]
  * [cite_start]**2e)** Avoid both exits and the cliff (so an episode should never terminate) [cite: 126]

[cite_start]To see what behavior a set of numbers ends up in, run the following command: [cite: 127]

```bash
python gridworld.py -g DiscountGrid -a value --discount [YOUR_DISCOUNT] --noise [YOUR_NOISE] --livingReward [YOUR_LIVING_REWARD]
```

[cite_start][cite: 128, 129]

**Notes:**

  * [cite_start]`question2a()` through `question2e()` should each return a 3-item tuple of `(discount, noise, living reward)` in `analysis.py`. [cite: 131]
  * You can check your policies in the GUI. [cite_start]For example, using a correct answer to 2a: the arrow in (0,1) should point east, the arrow in (1,1) should also point east, and the arrow in (2,1) should point north. [cite: 132]
  * On some machines, you may not see an arrow. [cite_start]In this case, press a button on the keyboard to switch to qValue display, and mentally calculate the policy by taking the arg max of the available qValues for each state. [cite: 133, 134]

**Grading:**

  * [cite_start]We will check that the desired policy is returned in each case. [cite: 136]
  * [cite_start]You can run the autograder to check your points: [cite: 137]
    ```bash
    python autograder.py -q q2
    ```
    [cite_start][cite: 138]

-----

## Q3 (5 pts). Q-Learning

[cite_start]**Update this file:** `qlearningAgents.py` [cite: 141, 142]

[cite_start]You will now write a Q-learning agent, which learns by trial and error from interactions with the environment through its update `(state, action, nextState, reward)` method. [cite: 144] [cite_start]A stub of a Q-learner is specified in `QLearningAgent` in `qlearningAgents.py`. [cite: 145]

[cite_start]For this question, you must implement the `update`, `computeValueFromQValues`, `getQValue`, and `computeActionFromQValues` methods. [cite: 146]

**Important Notes:**

  * For `computeActionFromQValues`, you should break ties randomly for better behavior. [cite_start]The `random.choice()` function will help. [cite: 147]
  * [cite_start]In a particular state, actions that your agent hasn't seen before still have a Q-value, specifically a Q-value of zero, and if all of the actions that your agent has seen before have a negative Q-value, an unseen action may be optimal. [cite: 148]
  * [cite_start]Make sure that in your `computeValueFromQValues` and `computeActionFromQValues` functions, you only access Q values by calling `getQValue`. [cite: 149] [cite_start]This abstraction will be useful for later Q6 when you override `getQValue` to use features of state-action pairs rather than state-action pairs directly. [cite: 150]

**Hint:**
With the Q-learning update in place, you can watch your Q-learner learn under manual control. [cite_start]To help with debugging, you can turn off noise by using the `--noise 0.0` parameter. [cite: 151, 152]

[cite_start]If you manually steer Pacman north and then east along the optimal path for four episodes (`-k 4`), you should see the following Q-values: [cite: 153]

```bash
python gridworld.py -a q -k 4 --noise 0.0 -m
```

[cite_start][cite: 154]

[cite_start]**Expected Q-Values:** [cite: 155-181]

  * 0.00
  * 0.05, 0.00
  * 0.25, 0.00, 0.62, 0.94
  * 10.00 (terminal state)

**Grading:**

  * [cite_start]We will run your Q-learning agent and check that it learns the same Q-values and policy as our reference implementation when each is presented with the same set of examples. [cite: 186]
  * [cite_start]To grade your implementation, run the autograder: [cite: 188]
    ```bash
    python autograder.py -q q3
    ```
    [cite_start][cite: 189]

-----

## Q4 (2 pts). Epsilon Greedy

[cite_start]**Update this file:** `qlearningAgents.py` [cite: 190, 191]

[cite_start]Complete your Q-learning agent by implementing epsilon-greedy action selection in `getAction`, meaning it chooses random actions an epsilon fraction of the time, and follows its current best Q-values otherwise. [cite: 192]

**Notes:**

  * [cite_start]Choosing a random action may result in choosing the best action; that is, you should not choose a random sub-optimal action, but rather any random legal action. [cite: 193]
  * [cite_start]You can choose an element from a list uniformly at random by calling the `random.choice` function. [cite: 194]
  * [cite_start]You can simulate a binary variable with probability $p$ of success by using `util.flipCoin(p)`, which returns `True` with probability $p$ and `False` with probability $1-p$. [cite: 195]

[cite_start]After implementing the `getAction` method, observe the behavior of the agent in Gridworld (with epsilon = 0.3): [cite: 196]

```bash
python gridworld.py -a q -k 100
```

[cite_start][cite: 197]

[cite_start]Your final Q-values should resemble those of your value iteration agent, especially along well-traveled paths. [cite: 198] [cite_start]However, your average returns will be lower than the Q-values predict because of the random actions and the initial learning phase. [cite: 199]

[cite_start]You can also observe the following simulations for different epsilon values: [cite: 200]

```bash
python gridworld.py -a q -k 100 --noise 0.0 -e 0.1
python gridworld.py -a q -k 100 --noise 0.0 -e 0.9
```

[cite_start][cite: 202]

**Crawler Robot:**
[cite_start]With no additional code, you should now be able to run a Q-learning crawler robot: [cite: 206]

```bash
python crawler.py
```

[cite_start][cite: 207]

  * [cite_start]If this doesn't work, you've probably written some code too specific to the GridWorld problem and you should make it more general to all MDPs. [cite: 208]
  * [cite_start]Play around with the various learning parameters to see how they affect the agent's policies and actions. [cite: 210]
  * [cite_start]Note that the step delay is a parameter of the simulation, whereas the learning rate and epsilon are parameters of your learning algorithm, and the discount factor is a property of the environment. [cite: 211]

**Grading:**
[cite_start]To grade your implementation, run the autograder: [cite: 213]

```bash
python autograder.py -q q4
```

[cite_start][cite: 213]

-----

## Q5 (1 pts). Q-Learning and Pacman

[cite_start]**(Optionally) update this file:** `qlearningAgents.py` [cite: 214, 215]

Time to play some Pacman\! [cite_start]Pacman will play games in two phases. [cite: 216]

1.  **Training:** Pacman will begin to learn about the values of positions and actions. [cite_start]Because it takes a very long time to learn accurate Q-values even for tiny grids, Pacman's training games run in quiet mode by default, with no GUI (or console) display. [cite: 217, 218]
2.  **Testing:** Once Pacman's training is complete, he will enter testing mode. When testing, Pacman's `self.epsilon` and `self.alpha` will be set to 0.0, effectively stopping Q-learning and disabling exploration, in order to allow Pacman to exploit his learned policy. [cite_start]Test games are shown in the GUI by default. [cite: 219-221]

[cite_start]Without any code changes, you should be able to run Q-learning Pacman for very tiny grids as follows: [cite: 222]

```bash
python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid
```

[cite_start][cite: 223]

**Notes:**

  * [cite_start]`PacmanQAgent` is already defined for you in terms of the `QLearningAgent` you've already written. [cite: 227]
  * [cite_start]`PacmanQAgent` is only different in that it has default learning parameters that are more effective for the Pacman problem (epsilon $= 0.05$, alpha $= 0.2$, gamma $= 0.8$). [cite: 228]
  * [cite_start]**Hint:** If your `QLearningAgent` works for `gridworld.py` and `crawler.py` but does not seem to be learning a good policy for Pacman on `smallGrid`, it may be because your `getAction` and/or `computeActionFromQValues` methods do not in some cases properly consider unseen actions. [cite: 229] [cite_start]In particular, because unseen actions have by definition a Q-value of zero, if all of the actions that have been seen have negative Q-values, an unseen action may be optimal. [cite: 230] [cite_start]Beware of the `argMax` function from `util.Counter`\! [cite: 231]
  * If you want to experiment with learning parameters, you can use the option `-a`, for example `-a epsilon=0.1,alpha=0.3,gamma=0.7`. [cite_start]These values will then be accessible as `self.epsilon`, `self.gamma` and `self.alpha` inside the agent. [cite: 232, 233]
  * While a total of 2010 games will be played, the first 2000 games will not be displayed because of the option `-x 2000`. [cite_start]Thus, you will only see Pacman play the last 10 of these games. [cite: 234, 235]
  * [cite_start]If you want to watch 10 training games to see what's going on, use the command: [cite: 237]
    ```bash
    python pacman.py -p PacmanQAgent -n 10 -l smallGrid -a numTraining=10
    ```
    [cite_start][cite: 238]

**Grading:**

  * [cite_start]You will receive full credit for this question if the command above works without exceptions and your agent wins at least 80% of the time. [cite: 240]
  * [cite_start]The autograder will run 100 test games after the 2000 training games. [cite: 242]
  * [cite_start]To grade your implementation, run the autograder: [cite: 243]
    ```bash
    python autograder.py -q q5
    ```
    [cite_start][cite: 244]

-----

## Q6 (3 pts). Approximate Q-Learning

[cite_start]**Update this file:** `qlearningAgents.py` [cite: 247, 248]

[cite_start]Implement an approximate Q-learning agent that learns weights for features of states, where many states might share the same features. [cite: 250] [cite_start]Write your implementation in `ApproximateQAgent` class in `qlearningAgents.py`, which is a subclass of `PacmanQAgent`. [cite: 251, 252]

[cite_start]**Note:** Approximate Q-learning assumes the existence of a feature function $f(s,a)$ over state and action pairs, which yields a vector $[f_{1}(s,a),...,f_{i}(s,a),...,f_{n}(s,a)]$ of feature values. [cite: 253] We provide feature functions for you in `featureExtractors.py`. [cite_start]Feature vectors are `util.Counter` (like a dictionary) objects containing the non-zero pairs of features and values; all omitted features have value zero. [cite: 254, 255]

[cite_start]The approximate Q-function takes the following form: [cite: 257]

$$Q(s,a) = \sum_{i=1}^{n} f_i(s, a)w_i$$
[cite_start][cite: 258, 259]

[cite_start]where each weight $w_{i}$ is associated with a particular feature $f_{i}(s,a)$. [cite: 261] [cite_start]In your code, you should implement the weight vector as a dictionary mapping features (which the feature extractors will return) to weight values. [cite: 262]

[cite_start]You will update your weight vectors similarly to how you updated Q-values: [cite: 263]

$$w_{i}\leftarrow w_{i}+\alpha \cdot \text{difference} \cdot f_{i}(s,a)$$
[cite_start][cite: 264]
$$\text{difference} = (r+\gamma \max_{a^{\prime}}Q(s^{\prime},a^{\prime}))-Q(s,a)$$
[cite_start][cite: 265, 266]

[cite_start]Note that the `difference` term is the same as in normal Q-learning, and $r$ is the experienced reward. [cite: 267]

By default, `ApproximateQAgent` uses the `IdentityExtractor`, which assigns a single feature to every (state, action) pair. [cite_start]With this feature extractor, your approximate Q-learning agent should work identically to `PacmanQAgent`. [cite: 268, 269] [cite_start]You can test this with the following command: [cite: 270]

```bash
python pacman.py -p ApproximateQAgent -x 2000 -n 2010 -l smallGrid
```

[cite_start][cite: 271]

**Important:**

  * [cite_start]`ApproximateQAgent` is a subclass of `QLearningAgent`, and it therefore shares several methods like `getAction`. [cite: 275]
  * [cite_start]Make sure that your methods in `QLearningAgent` call `getQValue` instead of accessing Q-values directly, so that when you override `getQValue` in your approximate agent, the new approximate q-values are used to compute actions. [cite: 276]

[cite_start]Once you're confident that your approximate learner works correctly with the identity features, run your approximate Q-learning agent with our custom feature extractor, which can learn to win with ease: [cite: 277]

```bash
python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumGrid
```

[cite_start][cite: 278]

[cite_start]If you have no errors, your approximate Q-learning agent should win almost every time with these simple features, even with only 50 training games. [cite: 279]

**Grading:**

  * [cite_start]We will run your approximate Q-learning agent and check that it learns the same Q-values and feature weights as our reference implementation when each is presented with the same set of examples. [cite: 282]
  * [cite_start]To grade your implementation, run the autograder: [cite: 283]
    ```bash
    python autograder.py -q q6
    ```
    [cite_start][cite: 284]

-----

## Contact & Warning

  * [cite_start]If you find any error in the grammar or project description, please contact the instructor via email: `hsmoon@cau.ac.kr`. [cite: 287]
  * [cite_start]**Plagiarism in code will result in an automatic F grade, regardless of the reason.** [cite: 289]
  * [cite_start]CAU has the internal system of detecting possible reuse of code. [cite: 290]
  * [cite_start]You may consult tools like ChatGPT for guidance, but **do not copy or submit generated content as-is.** This may lead to high similarity across submissions, which will be treated as plagiarism. [cite: 291, 292]