import requests


def fetch_hackerrank_profile(username):
    username = username.replace("@", "").strip()

    profile_url = f"https://www.hackerrank.com/profile/{username}"

    try:
        response = requests.get(
            profile_url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=10
        )

        if response.status_code not in [200, 301, 302]:
            return {
                "error": "Invalid HackerRank username"
            }

        return {
            "username": username,
            "name": username,
            "country": "N/A",
            "school": "N/A",
            "badges": 0,
            "profile_url": profile_url,
            "status": "Connected"
        }

    except Exception as e:
        return {
            "error": str(e)
        }