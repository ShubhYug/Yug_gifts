from fastapi import FastAPI
from database.database import Base, engine
from routes import users

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include user routes
app.include_router(users.router)
# app.include_router(product.router)
# app.include_router(order.router)


@app.get("/")
def home():
    return {"message": "Welcome to the E-commerce API!"}
