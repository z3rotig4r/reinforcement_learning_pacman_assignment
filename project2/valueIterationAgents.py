# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp: mdp.MarkovDecisionProcess, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        """
          Run the value iteration algorithm. Note that in standard
          value iteration, V_k+1(...) depends on V_k(...)'s.
        """
        numIter = self.iterations
        for idx in range(numIter):
            updatedVals = util.Counter()
            allStates = self.mdp.getStates()
            for s in allStates:
                if not self.mdp.isTerminal(s):
                    availableActions = self.mdp.getPossibleActions(s)
                    if len(availableActions) > 0:
                        qVals = [self.computeQValueFromValues(s, a) for a in availableActions]
                        updatedVals[s] = max(qVals)
            self.values = updatedVals

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        totalQ = 0.0
        transitions = self.mdp.getTransitionStatesAndProbs(state, action)
        for nextS, transProb in transitions:
            r = self.mdp.getReward(state, action, nextS)
            futureVal = self.discount * self.values[nextS]
            totalQ += transProb * (r + futureVal)
        return totalQ

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        if self.mdp.isTerminal(state):
            return None
        possibleActs = self.mdp.getPossibleActions(state)
        if len(possibleActs) == 0:
            return None
        optimalAct = None
        maxQ = float('-inf')
        for act in possibleActs:
            currQ = self.computeQValueFromValues(state, act)
            if currQ > maxQ:
                maxQ = currQ
                optimalAct = act
        return optimalAct

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
