def calculate_score(
    codeforces=None,
    leetcode=None,
    github=None,
    gfg=None,
    hackerrank=None,
    codechef=None
):
    score = 0

    if codeforces and not codeforces.get("error"):
        score += codeforces.get("rating", 0) * 0.5
        score += codeforces.get("solved_count", 0) * 2

    if leetcode and not leetcode.get("error"):
        score += leetcode.get("easy", 0)
        score += leetcode.get("medium", 0) * 2
        score += leetcode.get("hard", 0) * 3

    if github and not github.get("error"):
        score += github.get("public_repos", 0) * 5
        score += github.get("followers", 0) * 3

    if gfg and not gfg.get("error"):
        score += gfg.get("total_solved", 0) * 2
        score += gfg.get("coding_score", 0) * 0.5

    if hackerrank and not hackerrank.get("error"):
        score += hackerrank.get("badges", 0) * 20

    if codechef and not codechef.get("error"):
        score += codechef.get("rating", 0) * 0.4

    return round(score, 2)