from fastapi import FastAPI
from pydantic import BaseModel
from env import CSOpsEnv

app = FastAPI()
env = CSOpsEnv()

class Action(BaseModel):
    email_id: str | None = None
    category: str | None = None
    priority: str | None = None
    decision: str | None = None
    reply: str | None = None

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
def reset():
    return {"observation": env.reset()}

@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action.dict())
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return env.state()
