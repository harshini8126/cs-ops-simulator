from models import Observation, Action, Reward, Email
from tasks import TASKS

class CSOpsEnv:
    def __init__(self, task_name="easy"):
        self.task_name = task_name
        self.task = TASKS[task_name]
        self.reset()

    def reset(self):
        self.inbox = [Email(**e) for e in self.task["emails"]]
        self.processed = []
        self.time_left = self.task["time_limit"]
        self.satisfaction = 1.0
        self.done = False

        return Observation(
            inbox=self.inbox,
            processed=self.processed,
            time_left=self.time_left,
            satisfaction=self.satisfaction
        )

    def step(self, action: Action):
        if self.done:
            return self._get_obs(), Reward(score=0.0, reason="episode done"), True, {}

        reward = 0.0
        reasons = []

        email = next((e for e in self.inbox if e.id == action.email_id), None)

        if not email:
            return self._get_obs(), Reward(score=0.0, reason="invalid email"), False, {}

        gold = self.task["gold"][email.id]

        if action.category == gold["category"]:
            reward += 0.3
            reasons.append("correct category")
        else:
            reward -= 0.2
            reasons.append("wrong category")

        if action.priority == gold["priority"]:
            reward += 0.2
            reasons.append("correct priority")
        else:
            reasons.append("wrong priority")

        if action.decision == gold["decision"]:
            reward += 0.4
            reasons.append("correct decision")
        else:
            reward -= 0.3
            reasons.append("wrong decision")

        if action.reply and len(action.reply) > 15:
            reward += 0.1
            reasons.append("good reply")
        else:
            reasons.append("weak or no reply")

        if action.decision == "refund" and gold["decision"] != "refund":
            reward -= 0.4
            reasons.append("unnecessary refund")

        if action.decision == "ignore" and gold["priority"] == "high":
            reward -= 0.6
            reasons.append("ignored critical email")

        self.processed.append(email.id)
        self.inbox = [e for e in self.inbox if e.id != email.id]

        self.time_left -= 1

        if self.time_left <= 0:
            self.done = True
            reasons.append("time limit reached")

        if reward < 0:
            self.satisfaction -= 0.1
        else:
            self.satisfaction += 0.05

        self.satisfaction = max(0.0, min(1.0, self.satisfaction))

        if len(self.inbox) == 0:
            self.done = True
            reasons.append("all emails processed")

        reward = max(0.0, min(1.0, reward))

        return (
            self._get_obs(),
            Reward(score=reward, reason=", ".join(reasons)),
            self.done,
            {}
        )

    def state(self):
        return {
            "task": self.task_name,
            "time_left": self.time_left,
            "satisfaction": self.satisfaction,
            "remaining_emails": len(self.inbox)
        }

    def _get_obs(self):
        return Observation(
            inbox=self.inbox,
            processed=self.processed,
            time_left=self.time_left,
            satisfaction=self.satisfaction
        )