from prometheus_client import make_asgi_app
from fastapi import FastAPI, Response, status
import time
import os

app = FastAPI()

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.get("/")
def root():
    return {"ststus": "ok", "message": "mini service is running"}

@app.get("/health")
def health(fail: bool = False, response: Response = None):
    if fail:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "unhealthy"}
    return {"status": "healthy"}

@app.get("/slow")
def slow(ms: int = 300):
    time.sleep(ms / 1000)
    return {"status": "ok", "slept_ms": ms}

@app.get("/error")
def error(response: Response):
    response.status_code = 500
    return {"status": "error", "message": "simulated failure"}

@app.get("/version")
def version():
    app_version = os.getenv("APP_VERSION", "dev")
    return {"version": app_version}
 
