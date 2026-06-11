import re
import requests
from bs4 import BeautifulSoup


def fetch_codechef_profile(username):
    try:
        url = f"https://www.codechef.com/users/{username}"

        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10,
        )

        if response.status_code != 200:
            return {"error": "Invalid CodeChef username"}

        soup = BeautifulSoup(response.text, "html.parser")

        rating = 0
        stars = "N/A"
        highest_rating = 0

        rating_tag = soup.find("div", class_="rating-number")
        if rating_tag:
            rating = int(rating_tag.text.strip())

        star_tag = soup.find("span", class_="rating")
        if star_tag:
            stars = star_tag.text.strip()

        text = soup.get_text(" ", strip=True)
        high_match = re.search(r"Highest Rating\s*(\d+)", text)

        if high_match:
            highest_rating = int(high_match.group(1))

        return {
            "username": username,
            "rating": rating,
            "stars": stars,
            "highest_rating": highest_rating,
            "profile_url": url,
        }

    except Exception as e:
        return {"error": str(e)}