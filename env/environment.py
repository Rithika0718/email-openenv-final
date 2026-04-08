class EmailEnv:
    def __init__(self):
        self.step_count = 0

    def reset(self, task=None)::
        self.step_count = 0
        return {
            "email": "Congratulations! You won a prize. Click here now!"
        }

    def step(self, action):
        self.step_count += 1

        # simple reward logic
        if action.get("value") == "spam":
            reward = 1.0
        else:
            reward = 0.0

        done = self.step_count >= 5

        return (
            {"email": "Next email content"},
            reward,
            done,
            {}
        )
