import os
from openai import OpenAI
from env.environment import EmailEnv

API_BASE_URL = os.environ["API_BASE_URL"]
API_KEY = os.environ["API_KEY"]
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=API_KEY
)

def choose_action(observation):
    prompt = (
        "Classify the email.\n"
        "Return only: spam or not_spam.\n\n"
        f"{observation}"
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    result = response.choices[0].message.content.strip().lower()
    if result not in ["spam", "not_spam"]:
        return "spam"
    return result

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

            try:
                action_value = choose_action(obs)
            except Exception:
                action_value = "spam"

            try:
                obs, reward, done, info = env.step({"value": action_value})
                rewards.append(f"{reward:.2f}")

                print(f"[STEP] step={step} action=classify('{action_value}') reward={reward:.2f} done={str(done).lower()} error=null")

            except Exception as e:
                rewards.append("0.00")
                print(f"[STEP] step={step} action=classify('{action_value}') reward=0.00 done=false error={str(e)}")
                break

        success = done

    except Exception:
        success = False

    finally:
        if env is not None:
            try:
                env.close()
            except Exception:
                pass

        print(f"[END] success={str(success).lower()} steps={step} rewards={','.join(rewards)}")

if __name__ == "__main__":
    run_inference()
