from fastapi import APIRouter
from app.database.db import users_collection

from app.services.codeforces_service import fetch_codeforces_profile
from app.services.leetcode_service import fetch_leetcode_profile
from app.services.github_service import fetch_github_profile
from app.services.gfg_service import fetch_gfg_profile
from app.services.hackerrank_service import fetch_hackerrank_profile
from app.services.codechef_service import fetch_codechef_profile

from app.services.ai_service import (
    generate_ai_insights,
    generate_skill_recommendations,
)

from app.utils.scoring import calculate_score

router = APIRouter()


PLATFORM_FETCHERS = {
    "codeforces": fetch_codeforces_profile,
    "leetcode": fetch_leetcode_profile,
    "github": fetch_github_profile,
    "gfg": fetch_gfg_profile,
    "hackerrank": fetch_hackerrank_profile,
    "codechef": fetch_codechef_profile,
}


@router.post("/add")
async def add_user(data: dict):
    name = data.get("name")

    if not name:
        return {"error": "Name is required"}

    existing_user = await users_collection.find_one({"name": name})

    old_platforms = existing_user.get("platforms", {}) if existing_user else {}
    updated_platforms = old_platforms.copy()

    for platform, fetcher in PLATFORM_FETCHERS.items():
        username = data.get(platform)

        if username:
            updated_platforms[platform] = fetcher(username)

    total_score = calculate_score(
        updated_platforms.get("codeforces"),
        updated_platforms.get("leetcode"),
        updated_platforms.get("github"),
        updated_platforms.get("gfg"),
        updated_platforms.get("hackerrank"),
        updated_platforms.get("codechef"),
    )

    user_doc = {
        "name": name,
        "platforms": updated_platforms,
        "total_score": total_score,
    }

    if existing_user:
        await users_collection.update_one(
            {"name": name},
            {"$set": user_doc}
        )

        return {
            "message": "User updated successfully"
        }

    await users_collection.insert_one(user_doc)

    return {
        "message": "User added successfully"
    }


@router.get("/leaderboard")
async def get_leaderboard():
    users = []

    cursor = users_collection.find().sort("total_score", -1)

    async for user in cursor:
        user["_id"] = str(user["_id"])
        users.append(user)

    return {
        "leaderboard": users
    }


@router.get("/compare/{user1}/{user2}")
async def compare_users(user1: str, user2: str):
    first = await users_collection.find_one({"name": user1})
    second = await users_collection.find_one({"name": user2})

    if not first or not second:
        return {
            "error": "One or both users not found"
        }

    first["_id"] = str(first["_id"])
    second["_id"] = str(second["_id"])

    winner = (
        first["name"]
        if first["total_score"] > second["total_score"]
        else second["name"]
    )

    return {
        "user1": {
            "name": first["name"],
            "score": first["total_score"],
            "platforms": first.get("platforms", {})
        },
        "user2": {
            "name": second["name"],
            "score": second["total_score"],
            "platforms": second.get("platforms", {})
        },
        "winner": winner
    }


@router.get("/profile/{name}")
async def get_profile(name: str):
    user = await users_collection.find_one({"name": name})

    if not user:
        return {
            "error": "User not found"
        }

    user["_id"] = str(user["_id"])

    return user


@router.get("/platform/{platform}/{username}")
async def get_platform_profile(platform: str, username: str):
    platform = platform.lower()

    fetcher = PLATFORM_FETCHERS.get(platform)

    if not fetcher:
        return {
            "error": "Unsupported platform"
        }

    return {
        "platform": platform,
        "username": username,
        "data": fetcher(username)
    }


@router.get("/insights/{name}")
async def get_ai_insights(name: str):
    user = await users_collection.find_one({"name": name})

    if not user:
        return {
            "error": "User not found"
        }

    user["_id"] = str(user["_id"])

    insights = generate_ai_insights(user)

    return {
        "name": name,
        "insights": insights
    }


@router.get("/recommendations/{name}")
async def get_ai_recommendations(name: str):
    user = await users_collection.find_one({"name": name})

    if not user:
        return {
            "error": "User not found"
        }

    user["_id"] = str(user["_id"])

    recommendations = generate_skill_recommendations(user)

    return {
        "name": name,
        "recommendations": recommendations
    }


@router.delete("/delete/{name}")
async def delete_user(name: str):
    result = await users_collection.delete_one({"name": name})

    if result.deleted_count == 0:
        return {
            "error": "User not found"
        }

    return {
        "message": "User deleted successfully"
    }


@router.get("/{name}")
async def get_user(name: str):
    user = await users_collection.find_one({"name": name})

    if not user:
        return {
            "error": "User not found"
        }

    user["_id"] = str(user["_id"])

    return user