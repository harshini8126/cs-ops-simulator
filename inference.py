from env import CSOpsEnv
from models import Action


def get_action(email):
    subject = email["subject"].lower()
    body = email["body"].lower()
    urgency = email["urgency"]

    # Category
    if "billing" in subject or "charge" in body:
        category = "billing"
    elif "error" in body or "issue" in body:
        category = "technical"
    else:
        category = "general"

    # Priority
    priority = urgency

    # Decision
    if urgency == "high":
        decision = "escalate"
    else:
        decision = "reply"

    return Action(
        email_id=email["id"],
        category=category,
        priority=priority,
        decision=decision,
        reply="We will resolve your issue shortly."
    )


def run_task(task_name):
    print(f"[START] task={task_name}")

    env = CSOpsEnv(task_name)
    obs = env.reset()

    total_score = 0.0

    while obs["time_left"] > 0 and len(obs["inbox"]) > 0:
        email = obs["inbox"][0]

        action = get_action(email)

        obs, reward, done, _ = env.step(action)

        print(f"[STEP] email={email['id']} score={reward}")

        total_score += reward

        if done:
            break

    print(f"[END] task={task_name} total_score={total_score}")
    print()

if __name__ == "__main__":
    for task in ["easy", "medium", "hard"]:
        try:
            run_task(task)
        except Exception as e:
            print(f"[ERROR] task={task} error={str(e)}")
