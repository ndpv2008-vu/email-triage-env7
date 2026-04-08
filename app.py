import uvicorn
from fastapi import FastAPI
# Note the dots: these import from the files in your root directory
from env import EmailEnv
from models import Action

app = FastAPI()
env = EmailEnv()

@app.get("/")
def health():
    return {"status": "Email Triage Environment is Active"}

@app.post("/reset")
def reset():
    obs = env.reset()
    # Using .dict() as you requested for Pydantic models
    return obs.dict()

@app.post("/step")
def step(action: Action):
    result = env.step(action)
    return result

@app.get("/state")
def state():
    return env.state()

# This is the critical function for the [project.scripts] entry point
def main():
    print("Starting Email Triage Server on http://0.0.0.0:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
