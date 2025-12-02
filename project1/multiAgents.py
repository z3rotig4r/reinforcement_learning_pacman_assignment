# multiAgents.py
# --------------
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


from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Evaluation function for your reflex agent (question 1).

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        # Baseline
        score = successorGameState.getScore()
        
        # Food feature: 가장 가까운 음식으로 이동하도록 유도하기 위해 거리의 역수 사용
        foodList = newFood.asList()
        if foodList:
            closestFoodDistance = min([util.manhattanDist(newPos, food) for food in foodList])
            # Reciprocal distance - closer food = higher score
            score += 10.0 / (closestFoodDistance + 1)
        
        # Ghost feature: 거리와 scared 상태 모두 고려
        for ghostState in newGhostStates:
            ghostPosition = ghostState.getPosition()
            ghostDistance = util.manhattanDist(newPos, ghostPosition)
            
            # ghost의 scared 상태 조건
            if ghostState.scaredTimer > 0:
                # Chase scared ghosts for points
                if ghostDistance > 0:
                    score += 100.0 / ghostDistance
            else:
                # Avoid active ghosts - heavy penalty
                if ghostDistance <= 1:
                    # Immediate danger
                    score -= 500
                elif ghostDistance <= 2:
                    # Close danger
                    score -= 100
                else:
                    # Moderate distance - small penalty
                    score -= 10.0 / ghostDistance
        
        return score

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        def minimax(state, depth, agentIndex):
            # terminal state거나 depth 0일 때
            if state.isWin() or state.isLose() or depth == 0:
                return self.evaluationFunction(state)
            
            numAgents = state.getNumAgents()
            legalActions = state.getLegalActions(agentIndex)
            
            # Pacman's turn (maximizing)
            if agentIndex == 0:
                maxEval = float('-inf')
                for action in legalActions:
                    successor = state.generateSuccessor(agentIndex, action)
                    nextAgentIndex = 1
                    nextDepth = depth
                    eval = minimax(successor, nextDepth, nextAgentIndex)
                    maxEval = max(maxEval, eval)
                return maxEval
            # Ghost's turn (minimizing)
            else:
                minEval = float('inf')
                nextAgentIndex = (agentIndex + 1) % numAgents
                nextDepth = depth - 1 if nextAgentIndex == 0 else depth
                
                for action in legalActions:
                    successor = state.generateSuccessor(agentIndex, action)
                    eval = minimax(successor, nextDepth, nextAgentIndex)
                    minEval = min(minEval, eval)
                return minEval
        
        legalActions = gameState.getLegalActions(0)
        bestAction = None
        bestValue = float('-inf')
        
        for action in legalActions:
            successor = gameState.generateSuccessor(0, action)
            value = minimax(successor, self.depth, 1)
            if value > bestValue:
                bestValue = value
                bestAction = action
        
        return bestAction

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        def alphaBeta(state, depth, agentIndex, alpha, beta):
            # Terminal state 이거나 depth 0일 때
            if state.isWin() or state.isLose() or depth == 0:
                return self.evaluationFunction(state)
            
            numAgents = state.getNumAgents()
            legalActions = state.getLegalActions(agentIndex)
            
            # Pacman's turn (maximizing)
            if agentIndex == 0:
                maxEval = float('-inf')
                for action in legalActions:
                    successor = state.generateSuccessor(agentIndex, action)
                    nextAgentIndex = 1
                    nextDepth = depth
                    eval = alphaBeta(successor, nextDepth, nextAgentIndex, alpha, beta)
                    maxEval = max(maxEval, eval)
                    alpha = max(alpha, eval)
                    if beta < alpha:
                        break  # Beta cutoff
                return maxEval
            # Ghost's turn (minimizing)
            else:
                minEval = float('inf')
                nextAgentIndex = (agentIndex + 1) % numAgents
                nextDepth = depth - 1 if nextAgentIndex == 0 else depth
                
                for action in legalActions:
                    successor = state.generateSuccessor(agentIndex, action)
                    eval = alphaBeta(successor, nextDepth, nextAgentIndex, alpha, beta)
                    minEval = min(minEval, eval)
                    beta = min(beta, eval)
                    if beta < alpha:
                        break  # Alpha cutoff
                return minEval
        
        # Find best action
        legalActions = gameState.getLegalActions(0)
        bestAction = None
        bestValue = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        
        for action in legalActions:
            successor = gameState.generateSuccessor(0, action)
            value = alphaBeta(successor, self.depth, 1, alpha, beta)
            if value > bestValue:
                bestValue = value
                bestAction = action
            alpha = max(alpha, value)
            # 루트 레벨에서는 (수행할) 행동을 선택해야 하므로 beta pruning X
        
        return bestAction

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        def expectimax(state, depth, agentIndex):
            # Terminal state 이거나 depth 0일 때
            if state.isWin() or state.isLose() or depth == 0:
                return self.evaluationFunction(state)
            
            numAgents = state.getNumAgents()
            legalActions = state.getLegalActions(agentIndex)
            
            # Pacman's turn (maximizing)
            if agentIndex == 0:
                maxEval = float('-inf')
                for action in legalActions:
                    successor = state.generateSuccessor(agentIndex, action)
                    nextAgentIndex = 1
                    nextDepth = depth
                    eval = expectimax(successor, nextDepth, nextAgentIndex)
                    maxEval = max(maxEval, eval)
                return maxEval
            # Ghost's turn (averaging)
            else:
                totalEval = 0
                nextAgentIndex = (agentIndex + 1) % numAgents
                nextDepth = depth - 1 if nextAgentIndex == 0 else depth
                
                for action in legalActions:
                    successor = state.generateSuccessor(agentIndex, action)
                    eval = expectimax(successor, nextDepth, nextAgentIndex)
                    totalEval += eval
                
                # Return average (expected value)
                return totalEval / len(legalActions)
        
        # Find best action
        legalActions = gameState.getLegalActions(0)
        bestAction = None
        bestValue = float('-inf')
        
        for action in legalActions:
            successor = gameState.generateSuccessor(0, action)
            value = expectimax(successor, self.depth, 1)
            if value > bestValue:
                bestValue = value
                bestAction = action
        
        return bestAction

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: This evaluation function combines multiple features to achieve
    high scores on the smallClassic layout. It considers:
    - Current game score (baseline)
    - Proximity to remaining food (reciprocal distance encourages hunting)
    - Proximity to capsules (power pellets for ghost hunting)
    - Ghost positions and scared timers (avoid or hunt based on state)
    - Number of remaining food pellets (penalize leaving food)
    - Distance to closest food as a tiebreaker
    """
    if currentGameState.isWin():
        return float('inf')
    if currentGameState.isLose():
        return float('-inf')
    
    score = currentGameState.getScore()
    pacmanPos = currentGameState.getPacmanPosition()
    ghostStates = currentGameState.getGhostStates()
    food = currentGameState.getFood()
    capsules = currentGameState.getCapsules()
    
    # Feature 1: Proximity to food
    foodList = food.asList()
    if foodList:
        closestFoodDistance = min([util.manhattanDist(pacmanPos, f) for f in foodList])
        score += 10.0 / (closestFoodDistance + 1)
    
    # Feature 2: Penalize number of remaining food
    score -= 0.5 * len(foodList)
    
    # Feature 3: Proximity to capsules
    if capsules:
        closestCapsuleDist = min([util.manhattanDist(pacmanPos, c) for c in capsules])
        score += 50.0 / (closestCapsuleDist + 1)
    
    # Feature 4: Ghost distances and scared timers
    for ghostState in ghostStates:
        ghostPosition = ghostState.getPosition()
        ghostDist = util.manhattanDist(pacmanPos, ghostPosition)
        scaredTimer = ghostState.scaredTimer
        
        if scaredTimer > 0:
            # ghost가 scared 상태면 hunting
            score += 200.0 / (ghostDist + 1)
        else:
            # ghost scared 아니면 피하기
            if ghostDist < 2:
                score -= 100.0  # Heavy penalty
            elif ghostDist < 4:
                score -= 50.0 / (ghostDist + 1)
            else:
                score -= 10.0 / (ghostDist + 1)
    
    # Feature 5: Bonus for clearing the board
    score += 10 * (len(foodList) == 0)
    
    return score

# Abbreviation
better = betterEvaluationFunction