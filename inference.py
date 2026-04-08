from env import CSOpsEnv
from models import Action
import os

client = None
MODEL = os.environ.get("MODEL_NAME", "gpt-4o-mini")

if os.environ.get("API_BASE_URL") and os.environ.get("API_KEY"):
    from openai import OpenAI
    client = OpenAI(
        base_url=os.environ.get("API_BASE_URL"),
        api_key=os.environ.get("API_KEY")
    )


def get_action(email):
    if client:
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": f"""
Classify this email and decide action.

Subject: {email["subject"]}
Body: {email["body"]}
Urgency: {email["urgency"]}

Return: category, priority, decision
"""
                    }
                ],
                temperature=0
            )

            text = response.choices[0].message.content.lower()

            category = "general"
            if "billing" in text:
                category = "billing"
            elif "technical" in text:
                category = "technical"

            priority = email["urgency"]
            if "high" in text:
                priority = "high"

            decision = "reply"
            if "escalate" in text:
                decision = "escalate"

            return Action(
                email_id=email["id"],
                category=category,
                priority=priority,
                decision=decision,
                reply="Handled"
            )

        except Exception:
            pass  # fallback

    return Action(
        email_id=email["id"],
        category="general",
        priority=email["urgency"],
        decision="reply",
        reply="Handled"
    )


def run_task(task):
    print(f"[START] task={task}")

    env = CSOpsEnv(task)
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

    print(f"[END] task={task} total_score={total_score}")


if __name__ == "__main__":
    for t in ["easy", "medium", "hard"]:
        try:
            run_task(t)
        except Exception as e:
            print(f"[ERROR] task={t} error={str(e)}")
