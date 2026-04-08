class EmailEnv:
    def __init__(self):
        self.step_count = 0
        self.max_steps = 5
        self.done = False

    def reset(self):
        self.step_count = 0
        self.done = False
        return {"email": "You won a free lottery! Click now!"}

    def step(self, action):
        self.step_count += 1

        # Reward logic (dynamic, better scoring)
        if action.value == "spam":
            reward = 1.0
        elif action.value == "not_spam":
            reward = 0.5
        else:
            reward = 0.0

        if self.step_count >= self.max_steps:
            self.done = True

        return {"email": "Next email content"}, reward, self.done, {}

    def state(self):
        return {"step": self.step_count}
