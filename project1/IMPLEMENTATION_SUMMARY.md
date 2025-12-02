# Pacman AI Assignment - Implementation Summary

**Status: ✅ COMPLETE - 20/20 Points (Perfect Score)**

## Final Results

| Question | Implementation | Points | Status |
|----------|-----------------|--------|--------|
| Q1 | ReflexAgent | 4/4 | ✅ PASS |
| Q2 | MinimaxAgent | 4/4 | ✅ PASS |
| Q3 | AlphaBetaAgent | 3/3 | ✅ PASS |
| Q4 | ExpectimaxAgent | 3/3 | ✅ PASS |
| Q5 | betterEvaluationFunction | 6/6 | ✅ PASS |
| **TOTAL** | **All 5 Questions** | **20/20** | **✅ PERFECT** |

---

## Implementation Details

### Q1: ReflexAgent (4/4 points)
**File:** `multiAgents.py` - `ReflexAgent.evaluationFunction()`

**Strategy:**
- Evaluates state-action pairs (not just states)
- Returns `-inf` if action leads to ghost collision
- Combines multiple features with weighted scoring:
  - **Food proximity**: Uses reciprocal distance `10.0 / (closestFoodDist + 1)` to encourage food hunting
  - **Ghost avoidance**: Penalizes moves close to ghosts (distance < 3)
  - **Scared ghost hunting**: When ghosts are scared (have scaredTimer > 0), actively hunts them
  - **Baseline score**: Uses game score as foundation

**Key Achievement:**
- Wins all 10 games on openClassic layout
- Average score: 1226.2 (>1000 bonus points earned)
- No timeouts

---

### Q2: MinimaxAgent (4/4 points)
**File:** `multiAgents.py` - `MinimaxAgent.getAction()`

**Algorithm:**
- Recursive minimax with depth-limited search
- Handles arbitrary number of ghosts correctly
- **Depth management:** Decrements only after Pacman + all ghosts move (one ply)
- **Agent rotation:** Correctly cycles through agents 0→1→...→N→0

**Implementation Logic:**
```
minimax(state, depth, agentIndex):
  if terminal or depth == 0:
    return evaluationFunction(state)
  
  if agentIndex == 0 (Pacman):
    return max over legal actions of minimax(successor, depth, 1)
  else (Ghost):
    return min over legal actions of minimax(successor, nextDepth, nextAgent)
```

**Key Achievement:**
- Passes all 33 test cases
- Correctly explores game trees with 1+ ghosts at various depths
- All evaluation tests pass

---

### Q3: AlphaBetaAgent (3/3 points)
**File:** `multiAgents.py` - `AlphaBetaAgent.getAction()`

**Algorithm:**
- Standard alpha-beta pruning with strict inequality cutoff (`beta < alpha`)
- **Pruning Condition:** Uses `<` (not `<=`) to minimize over-pruning
  - `<= ` would prune too aggressively and miss valid nodes
  - `<` allows tied values to be explored fully
- **Root level:** Maintains alpha across root action iterations but doesn't prune at root (to ensure best action selection)

**Key Insight:**
- Tied values at root require full exploration (test_cases/q3/6-tied-root.test)
- Strict inequality ensures node C is explored even when min2 would return 10 (matching min1's value)

**Key Achievement:**
- Passes all 34 test cases including complex tree structures
- Properly handles tied-root scenarios
- Correct node generation with minimal pruning

---

### Q4: ExpectimaxAgent (3/3 points)
**File:** `multiAgents.py` - `ExpectimaxAgent.getAction()`

**Algorithm:**
- Models ghosts as random agents (uniform probability over legal moves)
- Pacman still maximizes; ghosts average (expected value)

**Implementation Logic:**
```
expectimax(state, depth, agentIndex):
  if terminal or depth == 0:
    return evaluationFunction(state)
  
  if agentIndex == 0 (Pacman):
    return max over legal actions
  else (Ghost):
    return average of all action values (sum / count)
```

**Key Achievement:**
- Wins ~50% of trappedClassic games (compared to AlphaBeta losing)
- Correctly averages ghost moves instead of minimizing
- Passes all 16 test cases

---

### Q5: betterEvaluationFunction (6/6 points)
**File:** `multiAgents.py` - `betterEvaluationFunction()`

**Strategy:**
Sophisticated state evaluation combining 5 key features:

1. **Game Score Baseline** - Use currentGameState.getScore()
2. **Food Proximity** - Reciprocal distance: `10.0 / (closestFoodDist + 1)`
   - Encourages Pacman to chase nearby food
3. **Food Count Penalty** - Subtract `0.5 * numFoodRemaining`
   - Penalizes leaving food on the board
4. **Capsule Hunting** - High weight `50.0 / (closestCapsuleDist + 1)`
   - Power pellets enable ghost hunting
5. **Ghost Behavior** - Conditional based on scaredTimer:
   - **Scared ghosts** (+): Hunt with `200.0 / (ghostDist + 1)`
   - **Normal ghosts** (-): Avoid with varying penalties based on distance

**Scoring Scheme:**
- `d < 2`: Harsh penalty (`-100.0`) for immediate collision risk
- `d < 4`: Medium penalty (`-50.0 / (d+1)`) for danger zone
- `d >= 4`: Light penalty (`-10.0 / (d+1)`) for awareness

**Performance on smallClassic:**
- Average score: **1071.7** (>1000 threshold met)
- Win rate: **10/10 games** (100%)
- Execution time: ~30 seconds per game with --no-graphics (acceptable)
- All scoring bonuses earned (6/6 points)

---

## Testing & Verification

### Test Commands Used
```bash
# Individual question testing
python autograder.py -q q1 --mute
python autograder.py -q q2 --mute
python autograder.py -q q3 --mute
python autograder.py -q q4 --mute
python autograder.py -q q5 --mute

# Full autograder
python autograder.py --mute

# Manual gameplay
python pacman.py -p ReflexAgent -l openClassic
python pacman.py -p MinimaxAgent -l smallClassic -a depth=2
python pacman.py -p AlphaBetaAgent -l smallClassic -a depth=3
python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3
```

### All Tests Passing
- ✅ Q1: 1/1 test file, 4/4 points
- ✅ Q2: 33 test cases, 4/4 points
- ✅ Q3: 34 test cases, 3/3 points
- ✅ Q4: 16 test cases, 3/3 points
- ✅ Q5: 1 gameplay test file, 6/6 points

---

## Key Implementation Decisions

### 1. Reciprocal Distance Heuristics
Used `1.0 / (distance + 1)` instead of raw distances to:
- Avoid division by zero at distance 0
- Encourage shorter distances more strongly (exponential effect)
- Scale rewards appropriately

### 2. Depth Management (Critical)
- Depth decrements only after Pacman moves (when agent cycles back to 0)
- Not after every agent move
- Ensures "one ply" = Pacman + all ghosts moves

### 3. Alpha-Beta Cutoff Strategy
- Changed from `<=` to `<` to avoid excessive pruning
- Allows tied values to explore fully
- Root level explores all actions for proper decision-making

### 4. Ghost Behavior Differentiation
- **Q1/Q5:** Different handling of scared vs. normal ghosts
- **Q2:** Pure minimax assumes optimal opponent
- **Q3:** Same as Q2 with pruning optimization
- **Q4:** Models probabilistic (random) opponent behavior

---

## Submission Checklist

✅ Only `multiAgents.py` edited (no other files modified)
✅ All 5 questions implemented
✅ Perfect score: 20/20 points
✅ Passes all autograder tests
✅ Ready for submission by Oct 26 23:59 deadline

---

## Code Quality Features

- **No hardcoded agent indices** - Uses dynamic `numAgents`
- **Terminal state handling** - Proper win/lose/depth checks
- **Error prevention** - Avoids division by zero, handles empty food lists
- **Efficient pruning** - Alpha-beta significantly reduces computation vs. pure minimax
- **Clear comments** - Each section documented

---

**Submitted:** 2025-10-19
**Status:** ✅ Ready for submission
