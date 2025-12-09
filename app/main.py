from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api import credit

app = FastAPI()
app.include_router(credit.router)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")