import random

class CSOpsEnv:
    def __init__(self):
        self.time_left = 0
        self.inbox = []
        self.processed = []
        self.satisfaction = 1.0
        self.current_step = 0
        self.max_steps = 5

    def _generate_email(self):
        categories = ["billing", "technical", "spam", "general"]
        urgencies = ["low", "medium", "high"]
        return {
            "id": str(random.randint(1000, 9999)),
            "subject": "Sample Issue",
            "body": "This is a simulated customer email",
            "customer_id": str(random.randint(1, 100)),
            "urgency": random.choice(urgencies),
            "true_category": random.choice(categories)
        }

    def reset(self):
        self.time_left = self.max_steps
        self.inbox = [self._generate_email() for _ in range(3)]
        self.processed = []
        self.satisfaction = 1.0
        self.current_step = 0
        return self._get_observation()

    def step(self, action):
        reward = 0.0
        done = False

        if not self.inbox:
            done = True
            return self._get_observation(), reward, done, {}

        email = next((e for e in self.inbox if e["id"] == action.get("email_id")), None)

        if email:
            if action.get("category") == email["true_category"]:
                reward += 0.4
            if action.get("priority") == email["urgency"]:
                reward += 0.3

            decision = action.get("decision")
            if decision == "reply":
                reward += 0.2
            elif decision == "escalate":
                reward += 0.1
            elif decision == "ignore" and email["urgency"] == "high":
                reward -= 0.3

            self.inbox.remove(email)
            self.processed.append(email)

        self.time_left -= 1
        self.current_step += 1

        if self.time_left <= 0 or self.current_step >= self.max_steps:
            done = True

        self.satisfaction = max(0.0, self.satisfaction - 0.05)

        return self._get_observation(), reward, done, {}

    def state(self):
        return self._get_observation()

    def _get_observation(self):
        return {
            "inbox": self.inbox,
            "processed": [e["id"] for e in self.processed],
            "time_left": self.time_left,
            "satisfaction": self.satisfaction
        }
          
      
