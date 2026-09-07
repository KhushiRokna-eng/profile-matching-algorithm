"""
generate_data.py
Generates a synthetic dataset of user profiles for the
Profile-Based Matching Algorithm project.

Run this script once to create data/users.csv
"""

import random
import csv
from pathlib import Path
from faker import Faker

fake = Faker()

# --- Config ---
NUM_USERS = 150
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "data" / "users.csv"

MBTI_TYPES = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP",
]

CITIES = [
    "Bangalore", "Mumbai", "Delhi", "Hyderabad", "Pune",
    "Chennai", "Kolkata", "Jaipur", "Ahmedabad", "Chandigarh",
]

# Building blocks for realistic-sounding bios instead of pure gibberish
INTERESTS = [
    "hiking", "reading sci-fi novels", "playing chess", "cooking Italian food",
    "photography", "learning new languages", "open-source contributing",
    "playing the guitar", "running marathons", "watching documentaries",
    "painting", "gaming", "yoga", "traveling to new countries", "cycling",
]

WORK_STYLES = [
    "collaborative and thrive in team brainstorms",
    "independent and prefer deep focus work",
    "structured and like clear plans before starting",
    "flexible and adapt quickly to changing priorities",
    "detail-oriented and enjoy refining small things",
    "big-picture thinkers who like exploring new ideas",
]

PROFESSIONS = [
    "software engineer", "product manager", "data scientist",
    "UX designer", "marketing strategist", "backend developer",
    "machine learning engineer", "business analyst", "content writer",
    "financial analyst",
]

GOALS = [
    "build meaningful products that solve real problems",
    "grow into a leadership role over the next few years",
    "keep learning new technologies and stay hands-on",
    "transition into a more creative line of work",
    "start my own venture eventually",
    "mentor others while sharpening my own skills",
]


def generate_about_me():
    interest1, interest2 = random.sample(INTERESTS, 2)
    style = random.choice(WORK_STYLES)
    return (
        f"A little about me... I enjoy {interest1} and {interest2} in my free time. "
        f"At work, I'm {style}. I value honest conversations and good coffee."
    )


def generate_professional_summary():
    profession = random.choice(PROFESSIONS)
    goal = random.choice(GOALS)
    years = random.randint(1, 12)
    return (
        f"I'm a {profession} with {years} years of experience. "
        f"My goal is to {goal}."
    )


def generate_users(num_users=NUM_USERS):
    users = []
    for i in range(1, num_users + 1):
        user = {
            "user_id": i,
            "name": fake.name(),
            "about_me": generate_about_me(),
            "professional_summary": generate_professional_summary(),
            "mbti_type": random.choice(MBTI_TYPES),
            "location": random.choice(CITIES),
        }
        users.append(user)
    return users


def save_to_csv(users, path=OUTPUT_PATH):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=users[0].keys())
        writer.writeheader()
        writer.writerows(users)
    print(f"Saved {len(users)} synthetic user profiles to {path}")


if __name__ == "__main__":
    users = generate_users()
    save_to_csv(users)