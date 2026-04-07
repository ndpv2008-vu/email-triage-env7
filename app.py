from fastapi import FastAPI
from env import EmailTriageEnv
from models import Action

app = FastAPI()
env = EmailTriageEnv()


@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()


@app.post("/step")
def step(action: Action):
    result = env.step(action)
    return {
        "observation": result.observation.dict(),
        "reward": result.reward,
        "done": result.done,
        "info": result.info
    }


@app.get("/state")
def state():
    return env.state()