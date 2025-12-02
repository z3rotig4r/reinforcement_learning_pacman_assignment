# Project 2: Reinforcement Learning

**CSE 17182 Artificial Intelligence, Fall 2025**

이 프로젝트는 UC Berkeley의 Pacman AI 프로젝트를 기반으로 한 강화학습(Reinforcement Learning) 과제입니다.

## 📋 프로젝트 개요

Value Iteration과 Q-Learning 알고리즘을 구현하여 Gridworld, Crawler Robot, Pacman 환경에서 에이전트를 학습시킵니다.

## 🎯 최종 점수: 21/21 (만점)

| 문제 | 내용 | 배점 | 획득 |
|------|------|------|------|
| Q1 | Value Iteration | 5점 | ✅ 5/5 |
| Q2 | Bridge Crossing Analysis | 5점 | ✅ 5/5 |
| Q3 | Q-Learning | 5점 | ✅ 5/5 |
| Q4 | Epsilon Greedy | 2점 | ✅ 2/2 |
| Q5 | Q-Learning and Pacman | 1점 | ✅ 1/1 |
| Q6 | Approximate Q-Learning | 3점 | ✅ 3/3 |

---

## 🔧 구현 내용

### Q1: Value Iteration (`valueIterationAgents.py`)

MDP(Markov Decision Process)에서 Value Iteration 알고리즘을 구현했습니다.

**Value Iteration 업데이트 수식:**
$$V_{k+1}(s) \leftarrow \max_{a} \sum_{s'} T(s,a,s')[R(s,a,s') + \gamma V_k(s')]$$

#### 구현한 메서드:
- **`runValueIteration()`**: 지정된 반복 횟수만큼 value iteration 수행
- **`computeQValueFromValues(state, action)`**: 주어진 상태-행동 쌍의 Q-value 계산
- **`computeActionFromValues(state)`**: 현재 value function 기반 최적 행동 반환

```python
# Q-value 계산
Q(s,a) = Σ T(s,a,s') * [R(s,a,s') + γ * V(s')]
```

---

### Q2: Policies (`analysis.py`)

DiscountGrid에서 다양한 정책을 유도하기 위한 파라미터(discount, noise, livingReward) 설정:

| 문제 | 목표 정책 | discount | noise | livingReward |
|------|----------|----------|-------|--------------|
| 2a | 가까운 출구(+1), 절벽 위험 감수 | 0.2 | 0.0 | 0.0 |
| 2b | 가까운 출구(+1), 절벽 회피 | 0.2 | 0.2 | 0.0 |
| 2c | 먼 출구(+10), 절벽 위험 감수 | 0.9 | 0.0 | 0.0 |
| 2d | 먼 출구(+10), 절벽 회피 | 0.9 | 0.2 | 0.0 |
| 2e | 모든 출구/절벽 회피 (영원히 생존) | 0.9 | 0.2 | 11 |

**파라미터 선택 원리:**
- **discount**: 낮으면 가까운 보상 선호, 높으면 먼 보상도 고려
- **noise**: 높으면 절벽 근처가 위험해져 회피
- **livingReward**: 높으면 종료 상태를 피하고 계속 살아있으려 함

---

### Q3: Q-Learning (`qlearningAgents.py`)

모델 없이 경험을 통해 학습하는 Q-Learning 에이전트 구현:

**Q-Learning 업데이트 수식:**
$$Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma \max_{a'} Q(s',a') - Q(s,a)]$$

#### 구현한 메서드:
- **`__init__()`**: Q-values 저장을 위한 `util.Counter()` 초기화
- **`getQValue(state, action)`**: Q(s,a) 값 반환 (미방문 상태는 0.0)
- **`computeValueFromQValues(state)`**: $V(s) = \max_a Q(s,a)$
- **`computeActionFromQValues(state)`**: 최적 행동 선택 (동점 시 랜덤 선택)
- **`update(state, action, nextState, reward)`**: Q-value 업데이트

---

### Q4: Epsilon Greedy (`qlearningAgents.py`)

탐험(Exploration)과 활용(Exploitation)의 균형을 위한 ε-greedy 정책:

```python
def getAction(state):
    if random() < epsilon:
        return random_action()  # 탐험: 랜덤 행동
    else:
        return best_action()    # 활용: 최적 행동
```

- 확률 ε로 랜덤 행동 선택 (탐험)
- 확률 1-ε로 현재 최적 행동 선택 (활용)

---

### Q5: Q-Learning and Pacman

Q3, Q4에서 구현한 Q-Learning 에이전트가 Pacman 게임에서도 동작하는지 검증:

```bash
python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid
```

- 2000번 학습 후 100번 테스트에서 **100% 승률** 달성

---

### Q6: Approximate Q-Learning (`qlearningAgents.py`)

Feature 기반 Q-Learning으로 일반화 성능 향상:

**Approximate Q-function:**
$$Q(s,a) = \sum_{i=1}^{n} w_i \cdot f_i(s,a)$$

**Weight 업데이트:**
$$w_i \leftarrow w_i + \alpha \cdot \text{difference} \cdot f_i(s,a)$$
$$\text{difference} = [r + \gamma \max_{a'} Q(s',a')] - Q(s,a)$$

#### 구현한 메서드:
- **`getQValue(state, action)`**: feature vector와 weight의 내적으로 Q-value 계산
- **`update(state, action, nextState, reward)`**: TD error를 이용한 weight 업데이트

---

## 🚀 실행 방법

### 환경 설정
```bash
conda create -n pacman python=3.9 -y
conda activate pacman
```

### 테스트 실행
```bash
# 전체 테스트
python autograder.py

# 특정 문제만 테스트
python autograder.py -q q1
python autograder.py -q q2
# ...
```

### Gridworld 실행
```bash
# 수동 제어
python gridworld.py -m

# Value Iteration 에이전트
python gridworld.py -a value -i 100 -k 10

# Q-Learning 에이전트
python gridworld.py -a q -k 100
```

### Pacman 실행
```bash
# Q-Learning Pacman
python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid

# Approximate Q-Learning Pacman
python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumGrid
```

### Crawler Robot 실행
```bash
python crawler.py
```

---

## 📁 수정된 파일

과제 지침에 따라 다음 3개 파일만 수정되었습니다:

1. **`valueIterationAgents.py`** - Value Iteration 알고리즘 구현
2. **`qlearningAgents.py`** - Q-Learning 및 Approximate Q-Learning 구현
3. **`analysis.py`** - Bridge Crossing 분석 파라미터 설정

---

## 📚 참고 파일

- `mdp.py` - MDP 인터페이스 정의
- `learningAgents.py` - 에이전트 베이스 클래스
- `util.py` - 유틸리티 함수 (Counter 등)
- `gridworld.py` - Gridworld 환경
- `featureExtractors.py` - Approximate Q-Learning용 feature 추출기

---

## 🔑 핵심 알고리즘 요약

### Value Iteration vs Q-Learning

| 구분 | Value Iteration | Q-Learning |
|------|-----------------|------------|
| 유형 | Model-based (계획) | Model-free (학습) |
| MDP 필요 | ✅ 전이 확률 필요 | ❌ 경험으로 학습 |
| 수렴 | 반복 횟수로 보장 | 충분한 탐험 필요 |
| 적용 | 작은 상태 공간 | 대규모 환경 가능 |

### Approximate Q-Learning 장점

- **일반화**: 비슷한 상태들이 같은 feature를 공유
- **메모리 효율**: 모든 (s,a) 쌍 대신 weight만 저장
- **대규모 환경**: Pacman 같은 큰 상태 공간에서도 학습 가능

