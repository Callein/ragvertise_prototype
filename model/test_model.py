from pydantic import BaseModel


class GenerateTestRequest(BaseModel):
    system_prompt: str
    user_prompt: str
