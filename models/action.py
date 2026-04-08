from pydantic import BaseModel

class Action(BaseModel):
    action_type: str   # classify / prioritize / reply
    value: str         # spam/work/personal OR reply text