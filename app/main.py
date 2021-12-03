from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credential=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/health-check/")
def health_check():
    return "OK"