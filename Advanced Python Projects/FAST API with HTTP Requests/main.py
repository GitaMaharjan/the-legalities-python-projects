# 31.  FAST API with HTTP Requests   
#     *Description*: Create a program that interacts with a public REST API using HTTP requests.  
#     *Skills*: Working with APIs, JSON handling, error handling.

# Import necessary libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import httpx

# Define the User model using Pydantic's BaseModel
# This model enforces structure and type validation on user data.
class User(BaseModel):
    id: int      # Integer ID of the user
    name: str    # Name of the user
    email: str   # Email of the user

# Initialize the FastAPI application
app = FastAPI()

# Define the base URL of the public API that we will fetch data from.
API_URL = "https://jsonplaceholder.typicode.com/users"

# Create a GET endpoint to retrieve a list of users from the external API.
@app.get("/users/", response_model=List[User])
async def get_users():
    # Use httpx.AsyncClient to make an asynchronous request to the public API.
    # Asynchronous operations allow the server to handle multiple requests efficiently.
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL)  # Send a GET request to fetch users.
        # If the response status is not 200 (OK), raise an HTTPException with the appropriate status code.
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching users")
        # Return the JSON response directly if the request was successful.
        return response.json()

# Create another GET endpoint to retrieve a specific user by ID from the external API.
# The user_id is passed as a path parameter and the response is validated as a single User model.
@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    # Again, use httpx.AsyncClient for making asynchronous HTTP requests.
    async with httpx.AsyncClient() as client:
        # Send a GET request to fetch a user with the specified ID.
        response = await client.get(f"{API_URL}/{user_id}")
        # If the response status is not 200 (OK), raise an HTTPException indicating the user was not found.
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="User not found")
        # Return the JSON data for the specific user.
        return response.json()
