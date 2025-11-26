from fastapi import FastAPI
from routers.routes import router

app = FastAPI()

# -----------------------------
#   ROUTERS
# -----------------------------
app.include_router(router)


# -----------------------------
#   ROOT
# -----------------------------
@app.get("/")
def root():
    return {"message": "Assistant API running"}