import requests


def fetch_codeforces_profile(handle):
    try:
        user_url = f"https://codeforces.com/api/user.info?handles={handle}"
        sub_url = f"https://codeforces.com/api/user.status?handle={handle}"

        user_res = requests.get(user_url, timeout=10).json()

        if user_res.get("status") != "OK":
            return {"error": "Invalid Codeforces handle"}

        user = user_res["result"][0]

        sub_res = requests.get(sub_url, timeout=10).json()
        solved = set()

        if sub_res.get("status") == "OK":
            for sub in sub_res["result"]:
                if sub.get("verdict") == "OK":
                    problem = sub.get("problem", {})
                    solved.add(f"{problem.get('contestId')}-{problem.get('index')}")

        return {
            "handle": handle,
            "rating": user.get("rating", 0),
            "max_rating": user.get("maxRating", 0),
            "rank": user.get("rank", "N/A"),
            "solved_count": len(solved),
            "profile_url": f"https://codeforces.com/profile/{handle}",
        }

    except Exception as e:
        return {"error": str(e)}