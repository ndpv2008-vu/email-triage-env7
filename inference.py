import os
from openai import OpenAI
from env import EmailTriageEnv
from models import Action

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

env = EmailTriageEnv()

obs = env.reset()
total_reward = 0

for step in range(5):
    email_text = f"{obs.subject} {obs.body}"

    if "win" in email_text.lower():
        action = Action(action_type="classify", value="spam")
    elif "boss" in obs.sender:
        action = Action(action_type="classify", value="important")
    else:
        action = Action(action_type="prioritize", value="low")

    result = env.step(action)
    obs = result.observation
    total_reward += result.reward

    if result.done:
        break

print("Final Reward:", total_reward)