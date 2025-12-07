from fastapi import FastAPI
import models
from database import engine
from routers import students, instructors, departments, courses, registrations

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="University Course Registration API")

app.include_router(departments.router)
app.include_router(students.router)
app.include_router(instructors.router)
app.include_router(courses.router)
app.include_router(registrations.router)
