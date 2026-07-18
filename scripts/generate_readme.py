import csv
from datetime import datetime

def read_problems(filepath="problems.csv"):
    problems = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            problems.append(row)
    return sorted(problems, key=lambda x: int(x["number"]))

def get_difficulty_emoji(diff):
    return {"Easy": "🟢 Easy", "Medium": "🟡 Medium", "Hard": "🔴 Hard"}.get(diff, diff)

def get_difficulty_badge_color(diff):
    return {"Easy": "00b8a3", "Medium": "ffc01e", "Hard": "ef4743"}.get(diff, "gray")

def generate_readme(problems):
    easy   = [p for p in problems if p["difficulty"] == "Easy"]
    medium = [p for p in problems if p["difficulty"] == "Medium"]
    hard   = [p for p in problems if p["difficulty"] == "Hard"]
    total  = len(problems)

    e, m, h = len(easy), len(medium), len(hard)

    # Language breakdown
    lang_count = {}
    for p in problems:
        lang_count[p["language"]] = lang_count.get(p["language"], 0) + 1
    total_lang = sum(lang_count.values())
    lang_pct = {k: round(v / total_lang * 100, 1) for k, v in lang_count.items()}

    lang_badge_map = {
        "Python":     ("3776AB", "python",     "white"),
        "C":          ("A8B9CC", "c",           "white"),
        "Java":       ("007396", "oracle",      "white"),
        "JavaScript": ("F7DF1E", "javascript",  "black"),
    }

    # Build problem table rows
    rows = []
    for p in problems:
        rows.append(
            f"| {p['number']} | {p['title']} "
            f"| {get_difficulty_emoji(p['difficulty'])} "
            f"| {p['language']} |"
        )
    table_rows = "\n".join(rows)

    # Build language badges
    lang_badges = []
    for lang, pct in lang_pct.items():
        color, logo, text_color = lang_badge_map.get(lang, ("555", lang.lower(), "white"))
        badge = (
            f"[![{lang}](https://img.shields.io/badge/{lang.replace(' ', '%20')}"
            f"-{pct}%25-{color}?style=for-the-badge&logo={logo}&logoColor={text_color})]"
            f"(./{lang.replace(' ', '_')})"
        )
        lang_badges.append(badge)
    lang_badges_str = "\n".join(lang_badges)

    updated = datetime.utcnow().strftime("%d %b %Y %H:%M UTC")

    readme = f"""<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=180&section=header&text=LeetCode%20Solutions&fontSize=42&fontColor=fff&animation=twinkling&fontAlignY=36&desc={total}%20Problems%20Solved%20%7C%20Python%20%C2%B7%20Java%20%C2%B7%20C%20%C2%B7%20JavaScript&descAlignY=58&descSize=16"/>

[![Profile](https://img.shields.io/badge/LeetCode-hari__preetham-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/hari_preetham/)
[![Problems Solved](https://img.shields.io/badge/Solved-{total}-success?style=for-the-badge&logo=checkmarx&logoColor=white)](https://github.com/Hari-preetham-B/LEET_CODE)
[![Languages](https://img.shields.io/badge/Languages-{len(lang_count)}-blue?style=for-the-badge&logo=python&logoColor=white)](https://github.com/Hari-preetham-B/LEET_CODE)
[![Last Updated](https://img.shields.io/badge/Updated-{updated.replace(' ', '%20').replace(':', '%3A')}-informational?style=for-the-badge)](https://github.com/Hari-preetham-B/LEET_CODE)

</div>

---

## 📊 Progress

<div align="center">

| Difficulty | Count | Badge |
|---|---|---|
| 🟢 Easy | {e} | ![Easy](https://img.shields.io/badge/Easy-{e}-00b8a3?style=flat-square) |
| 🟡 Medium | {m} | ![Medium](https://img.shields.io/badge/Medium-{m}-ffc01e?style=flat-square) |
| 🔴 Hard | {h} | ![Hard](https://img.shields.io/badge/Hard-{h}-ef4743?style=flat-square) |
| **Total** | **{total}** | ![Total](https://img.shields.io/badge/Total-{total}-blueviolet?style=flat-square) |

</div>

---

## 🗂️ Solutions by Language

<div align="center">

{lang_badges_str}

</div>

---

## 📋 Problem List

| # | Problem | Difficulty | Language |
|---|---------|-----------|----------|
{table_rows}

---

<div align="center">

> 💡 **"Every problem solved is a new pattern learned."**

*Auto-generated on {updated}*

[![Back to Profile](https://img.shields.io/badge/←%20Back%20to%20Profile-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Hari-preetham-B)

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=100&section=footer"/>

</div>
"""
    return readme

if __name__ == "__main__":
    problems = read_problems("problems.csv")
    readme   = generate_readme(problems)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    print(f"✅ README.md generated — {len(problems)} problems.")
