from .q_agent import DQNAgent, DQNetwork

def build_agent(state_dim=2, action_dim=4, learning_rate=0.01, discount_factor=0.95,
                 exploration_rate=1.0, exploration_decay=0.99995, min_exploration=0.001):
    return DQNAgent(state_dim, action_dim, learning_rate, discount_factor, exploration_rate,
                  exploration_decay, min_exploration)

def build_network(state_dim, action_dim):
    return DQNetwork(state_dim, action_dim)

def train_dqn(agent, env, episodes=100, max_steps=2000):
    for ep in range(episodes):
        state = env.reset()  # inital state
        total_reward = 0

        for step in range(max_steps):
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)

            # Save transition for replay buffer
            agent.store_experience(state, action, reward, next_state, done)

            # Update the network
            agent.learn()

            state = next_state
            total_reward += reward

            if done:
                print(f"Episode {ep+1} finished after {step+1} steps, total reward: {total_reward:.2f}")
                break

        # Optional: print epsilon to see how it decays
        print(f"Episode {ep+1}, Epsilon: {agent.epsilon:.3f}")

def get_agent_path(agent, env, max_steps=500):
    state = env.reset()
    path = [env.agent_pos.copy()]
    for _ in range(max_steps):
        action = agent.choose_action(state)
        next_state, _, done = env.step(action)
        path.append(env.agent_pos.copy())
        state = next_state
        if done:
            break
    return path