from env import CSOpsEnv
from models import Action

def get_action_from_llm(email):
    text = (email.subject + " " + email.body).lower()

    if "refund" in text or "charged" in text:
        return {"category": "billing", "priority": "high", "decision": "refund", "reply": "Refund initiated."}
    elif "crash" in text or "bug" in text:
        return {"category": "technical", "priority": "high", "decision": "escalate", "reply": "Tech team notified."}
    elif "lottery" in text:
        return {"category": "spam", "priority": "low", "decision": "ignore", "reply": ""}
    else:
        return {"category": "general", "priority": "low", "decision": "reply", "reply": "We will assist you."}


def run_task(task):
    env = CSOpsEnv(task)
    obs = env.reset()
    total = 0

    output_lines = []

    output_lines.append(f"[START] task={task}")

    done = False
    while not done:
        if not obs.inbox:
            break

        email = obs.inbox[0]
        data = get_action_from_llm(email)

        action = Action(
            email_id=email.id,
            category=data["category"],
            priority=data["priority"],
            decision=data["decision"],
            reply=data["reply"]
        )

        obs, reward, done, _ = env.step(action)
        total += reward.score

        output_lines.append(f"[STEP] email={email.id} score={reward.score}")

    output_lines.append(f"[END] task={task} total_score={total}\n")

    return "\n".join(output_lines)
