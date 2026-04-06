from env import CSOpsEnv
from models import Action

# Rule-based agent
def get_action(email):
    subject = email.subject.lower()
    body = email.body.lower()

    # Category
    if "refund" in body or "charge" in body or "billing" in subject:
        category = "billing"
    elif "error" in body or "bug" in body or "not working" in body:
        category = "technical"
    else:
        category = "general"

    # Priority
    if email.urgency >= 8:
        priority = "high"
    elif email.urgency >= 5:
        priority = "medium"
    else:
        priority = "low"

    # Decision
    if category == "billing":
        decision = "refund"
    elif category == "technical":
        decision = "escalate"
    else:
        decision = "respond"

    reply = "We have received your request and are processing it."

    return Action(
        email_id=email.id,
        category=category,
        priority=priority,
        decision=decision,
        reply=reply
    )


def run_task(task_name):
    print(f"[START] task={task_name}")

    env = CSOpsEnv(task_name)
    obs = env.reset()

    total_score = 0.0

    while obs.time_left > 0 and len(obs.inbox) > 0:
        email = obs.inbox[0]

        action = get_action(email)

        obs, reward, done, _ = env.step(action)

        # ✅ FIX: use reward.score instead of reward
        print(f"[STEP] email={email.id} score={reward.score}")

        total_score += reward.score

        if done:
            break

    print(f"[END] task={task_name} total_score={total_score}")
    print()


# MAIN
if __name__ == "__main__":
    for task in ["easy", "medium", "hard"]:
        run_task(task)
