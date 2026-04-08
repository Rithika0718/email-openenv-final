import os
from openai import OpenAI

from env.environment import EmailEnv

# ENV VARIABLES
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

def run_inference():
    env = EmailEnv()
    obs = env.reset()

    print(f"[START] task=email env=openenv model={MODEL_NAME}")

    rewards = []
    step = 0
    done = False

    while not done:
        step += 1

        # simple baseline action
        action_value = "spam"

        obs, reward, done, info = env.step(type("obj", (), {"value": action_value}))

        rewards.append(f"{reward:.2f}")

        print(f"[STEP] step={step} action=classify('{action_value}') reward={reward:.2f} done={str(done).lower()} error=null")

        if step > 5:
            break

    success = done

    print(f"[END] success={str(success).lower()} steps={step} rewards={','.join(rewards)}")


if __name__ == "__main__":
    try:
        run_inference()
    except Exception as e:
        print(f"[ERROR] {str(e)}")
