reward_log = {}

def update_rewards(chapter_id, version, reward):
    key = f"{chapter_id}_v{version}"
    reward_log.setdefault(key, []).append(reward)

def get_average_reward(chapter_id, version):
    key = f"{chapter_id}_v{version}"
    rewards = reward_log.get(key, [])
    return sum(rewards) / len(rewards) if rewards else 0
