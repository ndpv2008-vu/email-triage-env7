from models import Observation, Action, StepResult, Email


class EmailTriageEnv:
    def __init__(self):
        self.emails = [
            Email(email_id="1", sender="boss@company.com",
                  subject="Urgent meeting", body="Join ASAP"),
            Email(email_id="2", sender="spam@ads.com",
                  subject="Win money", body="Click here"),
        ]
        self.index = 0
        self.history = []
        self.done = False

    def reset(self):
        self.index = 0
        self.history = []
        self.done = False
        return self._get_obs()

    def state(self):
        return {"index": self.index, "history": self.history}

    def _get_obs(self):
        email = self.emails[self.index]
        return Observation(
            email_id=email.email_id,
            sender=email.sender,
            subject=email.subject,
            body=email.body,
            history=self.history,
            last_action_error=None
        )

    def step(self, action: Action):
        reward = 0.0
        email = self.emails[self.index]

        # RULES
        if action.action_type == "classify":
            if "spam" in email.sender and action.value == "spam":
                reward += 0.5
            elif "boss" in email.sender and action.value == "important":
                reward += 0.5
            else:
                reward -= 0.2

        elif action.action_type == "prioritize":
            if "boss" in email.sender and action.value == "high":
                reward += 0.5
            else:
                reward -= 0.2

        self.history.append(f"{action.action_type}:{action.value}")

        # move to next email
        self.index += 1
        if self.index >= len(self.emails):
            self.done = True
            self.index = len(self.emails) - 1

        return StepResult(
            observation=self._get_obs(),
            reward=reward,
            done=self.done,
            info={}
        )