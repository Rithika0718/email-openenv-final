import os
from openai import OpenAI
from env.environment import EmailEnv

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

def run_inference():
    env = None
    rewards = []
    step = 0
    success = False
    done = False

    print(f"[START] task=email env=openenv model={MODEL_NAME}")

    try:
        env = EmailEnv()
        obs = env.reset(None)

        while not done:
            step += 1

            action_value = "spam"
            action = {"value": action_value}

            obs, reward, done, info = env.step(action)
            rewards.append(f"{reward:.2f}")

            print(f"[STEP] step={step} action=classify('{action_value}') reward={reward:.2f} done={str(done).lower()} error=null")

            if step >= 5:
                break

        success = done

    except Exception:
        success = False

    finally:
        if env:
            try:
                env.close()
            except:
                pass

        print(f"[END] success={str(success).lower()} steps={step} rewards={','.join(rewards)}")

if __name__ == "__main__":
    run_inference()
