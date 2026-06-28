#Importing all the necessary librbaries
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

#Loading the environment variables from the .env file
load_dotenv()

#Creating the FastApi application
app = FastAPI(
    title="Utilize",
    description="An AI-Powered Personalized Household Bill Savings Advisor for London Households",
    version="1.0.0"
)

# Allow the React frontend to talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Test route - just to check the API is working
@app.get("/")
def home():
    return {
        "message": "Welcome to Utilize",
        "status": "running",
        "version": "1.0.0"
    }

# Health check route
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "app": "Utilize"
    }