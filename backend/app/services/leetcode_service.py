import requests


def fetch_leetcode_profile(username):
    url = "https://leetcode.com/graphql"

    query = """
    query getUserProfile($username: String!) {
      matchedUser(username: $username) {
        username
        submitStats {
          acSubmissionNum {
            difficulty
            count
          }
        }
      }
    }
    """

    try:
        response = requests.post(
            url,
            json={"query": query, "variables": {"username": username}},
            timeout=10
        )

        data = response.json()
        user = data.get("data", {}).get("matchedUser")

        if not user:
            return {"error": "Invalid LeetCode username"}

        result = {
            "username": username,
            "total_solved": 0,
            "easy": 0,
            "medium": 0,
            "hard": 0,
            "profile_url": f"https://leetcode.com/{username}",
        }

        for item in user["submitStats"]["acSubmissionNum"]:
            if item["difficulty"] == "All":
                result["total_solved"] = item["count"]
            elif item["difficulty"] == "Easy":
                result["easy"] = item["count"]
            elif item["difficulty"] == "Medium":
                result["medium"] = item["count"]
            elif item["difficulty"] == "Hard":
                result["hard"] = item["count"]

        return result

    except Exception as e:
        return {"error": str(e)}