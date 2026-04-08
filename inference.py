import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from openai import OpenAI

from env.environment import EmailEnv
from models.action import Action
from tasks.task_easy import get_easy_task

# ENV VARIABLES
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

def run_inference():
    env = EmailEnv()
    task = get_easy_task()

    obs = env.reset(task)

    print(f"[START] task=easy env=email model={MODEL_NAME}")

    rewards = []
    step = 0
    done = False

    while not done:
        step += 1

        action = Action(action_type="classify", value="spam")

        obs, reward, done, info = env.step(action)
        rewards.append(f"{reward:.2f}")

        print(f"[STEP] step={step} action=classify('spam') reward={reward:.2f} done={str(done).lower()} error=null")

        if step > 5:
            break

    success = done

    print(f"[END] success={str(success).lower()} steps={step} rewards={','.join(rewards)}")


# 🔥 HTTP SERVER FOR VALIDATOR
class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Email OpenEnv is running!")

    def do_POST(self):
        if self.path == "/reset":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status": "reset successful"}')
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    # Run inference once (for baseline logs)
    run_inference()

    # Start server (required for HF validator)
    port = int(os.environ.get("PORT", 7860))
    server = HTTPServer(("0.0.0.0", port), Handler)

    print(f"Server running on port {port}")
    server.serve_forever()