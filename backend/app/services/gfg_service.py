import requests


def fetch_gfg_profile(username):
    profile_url = f"https://www.geeksforgeeks.org/profile/{username}"

    try:
        response = requests.get(
            profile_url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )

        if response.status_code != 200:
            return {"error": "Invalid GFG username"}

        return {
            "username": username,
            "profile_url": profile_url,
            "status": "Connected",
            "total_solved": 0,
            "coding_score": 0,
            "school": 0,
            "basic": 0,
            "easy": 0,
            "medium": 0,
            "hard": 0,
            "institute_rank": "N/A"
        }

    except Exception as e:
        return {"error": str(e)}