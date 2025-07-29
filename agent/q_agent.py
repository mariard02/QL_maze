import random
import numpy as np

class QAgent:
    def __init__(self, learning_rate=0.1, discount_factor=0.99,
                 exploration_rate=1.0, exploration_decay=0.995, min_exploration=0.01):

        self.actions = [0, 1, 2, 3]  # e.g., [0, 1, 2, 3] for up/down/left/right
        self.q_table = {}       # {(state): [q_values_per_action]}
        self.alpha = learning_rate
        self.gamma = discount_factor
        self.epsilon = exploration_rate
        self.epsilon_decay = exploration_decay
        self.min_epsilon = min_exploration

    def get_q_values(self, state):
        if state not in self.q_table:
            self.q_table[state] = [0.0 for _ in self.actions]
        return self.q_table[state]
        
    def choose_action(self, state):
        p = random.random()

        if p < self.epsilon:
            chosen_action = random.choice(self.actions)
        else:
            q_values = self.get_q_values(state)
            chosen_action = np.argmax(q_values)
            self.epsilon *= self.epsilon_decay

        return chosen_action


    def learn(self, state, action, reward, next_state, done):

        q_values = self.get_q_values(state)
        current_q = q_values[action]

        if done:
            target = reward
        else:
            next_q_values = self.get_q_values(next_state)
            target = reward + self.gamma * max(next_q_values)

        q_values[action] += self.alpha * (target - current_q)
