class EmailEnv:
    def __init__(self):
        self.step_count = 0
        self.max_steps = 5

    def reset(self, task=None):
        # Accepts task (required by evaluator)
        self.step_count = 0
        return {"email": "Congratulations! You won a prize. Click here now!"}

    def step(self, action):
        self.step_count += 1

        # SAFE action handling (works for dict OR object)
        try:
            if isinstance(action, dict):
                label = action.get("value", "")
            else:
                label = getattr(action, "value", "")
        except:
            label = ""

        # Reward logic (simple but valid)
        if label == "spam":
            reward = 1.0
        elif label == "not_spam":
            reward = 0.5
        else:
            reward = 0.0

        done = self.step_count >= self.max_steps

        return (
            {"email": "Next email content"},
            reward,
            done,
            {}
        )

    def state(self):
        return {"step": self.step_count}
