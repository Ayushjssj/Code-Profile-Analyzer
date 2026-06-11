from fastapi import APIRouter
from app.database.db import users_collection

from app.utils.auth import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter()


@router.post("/signup")
async def signup(data: dict):

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    existing_user = await users_collection.find_one(
        {"email": email}
    )

    if existing_user:
        return {
            "error": "Email already exists"
        }

    user = {
        "name": name,
        "email": email,
        "password": hash_password(password)
    }

    await users_collection.insert_one(user)

    return {
        "message": "Signup successful"
    }


@router.post("/login")
async def login(data: dict):

    email = data.get("email")
    password = data.get("password")

    user = await users_collection.find_one(
        {"email": email}
    )

    if not user:
        return {
            "error": "Invalid credentials"
        }

    if not verify_password(
        password,
        user["password"]
    ):
        return {
            "error": "Invalid credentials"
        }

    token = create_access_token(
        {
            "email": user["email"]
        }
    )

    return {
        "access_token": token,
        "name": user["name"]
    }