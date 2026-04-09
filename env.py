import random

class CSOpsEnv:
    def __init__(self, task_name="easy"):
        self.task_name = task_name

        self.max_steps = 5
        self.num_emails = 3

        self.time_left = 0
        self.inbox = []
        self.processed = []

    def _generate_email(self):
        categories = ["billing", "technical", "spam", "general"]
        urgencies = ["low", "medium", "high"]
        return {
            "id": f"e{random.randint(1, 9999)}",
            "subject": "Sample Issue",
            "body": "Customer has a problem",
            "urgency": random.choice(urgencies),
            "true_category": random.choice(categories)
        }

    def reset(self):
        self.time_left = self.max_steps
        self.inbox = [self._generate_email() for _ in range(self.num_emails)]
        self.processed = []
        return self._get_obs()

    def step(self, action):
        reward = 0.0
        done = False

        if not self.inbox:
            return self._get_obs(), 0.2, True, {}

        email = self.inbox[0]

        if action.category == email["true_category"]:
            reward += 0.4
        if action.priority == email["urgency"]:
            reward += 0.3

        if action.decision == "reply":
            reward += 0.2
        elif action.decision == "escalate":
            reward += 0.1

        self.inbox.pop(0)
        self.processed.append(email)

        self.time_left -= 1
        if self.time_left <= 0:
            done = True

        # 🔥 STRICT SAFE RANGE (never 0 or 1)
        if reward <= 0:
            reward = 0.2
        elif reward >= 1:
            reward = 0.8
        else:
            reward = float(f"{reward:.3f}")

        return self._get_obs(), reward, done, {}

    def state(self):
        return self._get_obs()

    def _get_obs(self):
        return {
            "inbox": self.inbox,
            "time_left": self.time_left
        }
