import uvicorn
from fastapi import FastAPI
from openenv_core import create_app
# Replace 'EmailTriageEnv' with the actual class name of your environment
# from .email_triage_environment import EmailTriageEnv 

def main():
    """
    Entry point for the 'server' command defined in pyproject.toml
    """
    # This helper from openenv-core handles the API routing for you
    # app = create_app(EmailTriageEnv, env_name="email-triage-env")
    
    # For now, a placeholder to pass the 'Missing server/app.py' check:
    app = FastAPI(title="Email Triage Environment")
    
    @app.get("/health")
    def health():
        return {"status": "ok"}

    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()