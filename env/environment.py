class EmailEnv:
    def __init__(self):
        self.step_count = 0
        self.max_steps = 5
        self.current_task = "easy"

    def reset(self, task=None):
        self.step_count = 0
        # map task ids → 3 variants
        if task in ["easy_task", "easy"]:
            self.current_task = "easy"
            return {"email": "Win money now!!! Limited time offer!!!"}
        elif task in ["medium_task", "medium"]:
            self.current_task = "medium"
            return {"email": "Exclusive discount available just for you"}
        else:
            self.current_task = "hard"
            return {"email": "Hi team, please find the meeting agenda attached"}

    def step(self, action):
        self.step_count += 1

        # safe read
        try:
            label = action.get("value", "") if isinstance(action, dict) else getattr(action, "value", "")
        except:
            label = ""

        # ALL rewards strictly (0,1)
        if self.current_task == "easy":
            reward = 0.8 if label == "spam" else 0.3
        elif self.current_task == "medium":
            reward = 0.7 if label == "spam" else 0.4
        else:  # hard
            reward = 0.75 if label == "not_spam" else 0.2

        done = self.step_count >= self.max_steps

        return (
            {"email": "Next email content"},
            reward,
            done,
            {}
        )

    def state(self):
        return {"step": self.step_count, "task": self.current_task}

    def close(self):
        pass
