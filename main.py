from fastapi import FastAPI
from database import engine
import models
from routes import jobs

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Tracker API")

app.include_router(jobs.router)