from fastapi import FastAPI
from env import EmailEnv
from models import Action

app = FastAPI()
env = EmailEnv()

@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

@app.post("/step")
def step(action: Action):
    result = env.step(action)
    return result

@app.get("/state")
def state():
    return env.state()