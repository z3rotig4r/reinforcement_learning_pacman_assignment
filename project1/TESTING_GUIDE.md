# Quick Reference: How to Test & Submit

## ✅ Final Score: 20/20 Points (Perfect!)

### File to Submit
- **ONLY THIS FILE:** `multiAgents.py`
- **Deadline:** Oct 26 (Sun) 23:59
- **Submission Platform:** e-class system

### Quick Test Commands

```bash
# Test individual questions
python autograder.py -q q1      # ReflexAgent (4 pts)
python autograder.py -q q2      # MinimaxAgent (4 pts)
python autograder.py -q q3      # AlphaBetaAgent (3 pts)
python autograder.py -q q4      # ExpectimaxAgent (3 pts)
python autograder.py -q q5      # betterEvaluationFunction (6 pts)

# Test all questions
python autograder.py

# Test silently (no output spam)
python autograder.py --mute
```

### Manual Gameplay Testing

```bash
# Q1: Reflex Agent on openClassic (best layout for Q1)
python pacman.py -p ReflexAgent -l openClassic

# Q2: Minimax on smallClassic with depth 2
python pacman.py -p MinimaxAgent -l smallClassic -a depth=2

# Q3: Alpha-Beta on smallClassic with depth 3 (faster than minimax)
python pacman.py -p AlphaBetaAgent -l smallClassic -a depth=3

# Q4: Expectimax on trappedClassic (shows random ghost benefit)
python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3

# Q5: Better evaluation with depth 2
python pacman.py -p ExpectimaxAgent -l smallClassic -a evalFn=better -a depth=2
```

### What Each Question Does

| Q# | Agent | What It Does | Best Layout |
|----|-------|------------|------------|
| 1 | ReflexAgent | Evaluates single actions; fast & simple | openClassic |
| 2 | MinimaxAgent | Builds full game tree; assumes optimal ghosts | smallClassic |
| 3 | AlphaBetaAgent | Same as Q2 but faster (pruning) | smallClassic |
| 4 | ExpectimaxAgent | Models random ghosts; better at escaping traps | trappedClassic |
| 5 | betterEval | Advanced state evaluation; high scores | smallClassic |

### Expected Performance

**Q1 - Reflex Agent:**
- ✅ Wins: All 10 games
- ✅ Avg Score: >1200
- ✅ No Timeouts

**Q2 - Minimax Agent:**
- ✅ Passes: 33/33 test cases
- ✅ Nodes explored: Correct tree exploration

**Q3 - Alpha-Beta Agent:**
- ✅ Passes: 34/34 test cases
- ✅ Speed: Faster than minimax with same results
- ✅ Pruning: Efficient without over-pruning

**Q4 - Expectimax Agent:**
- ✅ Passes: 16/16 test cases
- ✅ Wins ~50% on trappedClassic (vs 0% for AlphaBeta)

**Q5 - Better Evaluation:**
- ✅ Wins: All 10 games
- ✅ Avg Score: 1071.7 (>1000 threshold)
- ✅ Speed: ~30s per game

### If You Get Errors

**Import errors?**
```bash
# Make sure you're in the project directory
cd /home/z3rotig4r/ai_packman_assignment/project1

# Check Python version
python --version  # Should be 3.7+
```

**Timeout errors?**
- AlphaBeta slower: Try smaller depth (-a depth=2)
- Expectimax slower: Try smaller depth (-a depth=2)

**Low scores?**
- Q1: Improve food/ghost heuristics
- Q5: Fine-tune feature weights

### Key Implementation Tips (If Modifying)

1. **Always use:** `util.manhattanDist(pos1, pos2)` for distances
2. **Never hardcode:** Ghost indices or agent counts
3. **Handle edge cases:** Empty food lists, terminal states
4. **Use reciprocals:** For distance-based heuristics: `1.0 / (distance + 1)`
5. **Depth management:** Decrement ONLY after all agents move

### File Structure

```
project1/
├── multiAgents.py          ← YOUR FILE (only one to submit!)
├── game.py                 (read-only: core engine)
├── pacman.py               (read-only: game rules)
├── layout.py               (read-only: map loading)
├── util.py                 (read-only: utilities)
├── autograder.py           (run tests)
├── test_cases/
│   ├── q1/, q2/, q3/, q4/, q5/  (test data)
├── layouts/                (game maps)
└── ...
```

### Submission Safety Checklist

- [ ] Only `multiAgents.py` is modified
- [ ] All 5 questions implemented
- [ ] All autograder tests pass (python autograder.py)
- [ ] No syntax errors (file runs without exceptions)
- [ ] Score is 20/20 before submitting
- [ ] Filename unchanged: `multiAgents.py`
- [ ] Submitted by Oct 26 23:59 deadline

---

**Status:** ✅ Ready to submit!
**Total Score:** 20/20 points (Perfect)
**File:** multiAgents.py (401 lines)
