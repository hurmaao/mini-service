from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import FastAPI, Response, status
import time
import os

app = FastAPI(redirect_slashes=False)

Instrumentator().instrument(app).expose(app)


@app.get("/")
def root():
    return {"status": "ok", "message": "mini service is running"}


@app.get("/health")
def health(response: Response, fail: bool = False):
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
