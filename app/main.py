from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "RUNNING"}

@app.get("/info")
def info():
    return {
        "service": "K8s Microservice",
        "version": "1.0",
        "author": "Harshal"
    }
