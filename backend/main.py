from fastapi import FastAPI

app = FastAPI(title="ASTRA API", version="1.0.0")


@app.get("/")
def root():
    return {
        "application": "ASTRA",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
