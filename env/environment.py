from models.action import Action

class EmailEnv:

    def __init__(self):
        self.reset()

    def reset(self, task=None):
        # Default fallback task
        if task is None:
            task = {
                "email": "You won a lottery! Click here!",
                "sender": "unknown@spam.com",
                "urgency": "low",
                "correct_label": "spam"
            }

        self.email = {
            "text": task["email"],
            "sender": task["sender"],
            "urgency": task["urgency"]
        }

        self.correct_label = task.get("correct_label", None)
        self.correct_priority = task.get("correct_priority", None)
        self.expected_reply = task.get("expected_reply", None)

        self.step_count = 0
        self.done = False

        return self._get_obs()

    def _get_obs(self):
        return Observation(
            email_text=self.email["text"],
            sender=self.email["sender"],
            urgency=self.email["urgency"],
            step_count=self.step_count
        )

    def step(self, action: Action):
        reward = 0

        # 1. Classification
        if action.action_type == "classify":
            if self.correct_label and action.value == self.correct_label:
                reward += 0.5
            else:
                reward -= 0.2

        # 2. Priority
        elif action.action_type == "prioritize":
            if self.correct_priority and action.value == self.correct_priority:
                reward += 0.3
            else:
                reward -= 0.1

        # 3. Reply
        elif action.action_type == "reply":
            if self.expected_reply and "sorry" in action.value.lower():
                reward += 0.5
                self.done = True
            else:
                reward -= 0.2

        # Step count increment
        self.step_count += 1

        # Penalty for too many steps
        if self.step_count > 5:
            reward -= 0.1

        return self._get_obs(), reward, self.done, {}

    def state(self):
        return {
            "email": self.email,
            "step_count": self.step_count,
            "done": self.done
        }
