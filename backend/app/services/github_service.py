import requests


def fetch_github_profile(username):
    try:
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return {"error": "Invalid GitHub username"}

        data = response.json()

        return {
            "username": data.get("login"),
            "name": data.get("name"),
            "public_repos": data.get("public_repos", 0),
            "followers": data.get("followers", 0),
            "following": data.get("following", 0),
            "avatar_url": data.get("avatar_url"),
            "profile_url": data.get("html_url"),
            "bio": data.get("bio"),
        }

    except Exception as e:
        return {"error": str(e)}