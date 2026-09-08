# Profile Matching Algorithm

A Python-based intelligent profile matching system that combines **NLP-based text similarity, MBTI personality compatibility, location compatibility, and user feedback** to generate ranked profile recommendations.

---

## Project Overview

The Profile Matching Algorithm is designed to identify compatible users based on both their **professional interests** and **personal characteristics**.

The system uses a hybrid recommendation approach by combining:

- Profile text similarity
- MBTI personality compatibility
- Location compatibility
- Historical user feedback

The goal is to produce a ranked list of users who are most compatible with a selected target user.

---

## Objective

The objective of this project is to develop an intelligent matching system that can:

1. Process structured and unstructured user profile information.
2. Measure similarity between users based on their profile descriptions.
3. Compare users using MBTI personality types.
4. Consider location as an additional compatibility factor.
5. Combine multiple compatibility signals into a single score.
6. Use previous user feedback to adapt the final compatibility score.
7. Rank and recommend the most compatible users.

---

## System Architecture

```text
                    User Profiles
                         │
                         ▼
                Profile Preprocessing
                         │
                         ▼
                  Cleaned Text
                         │
                         ▼
                   TF-IDF Vectorization
                         │
                         ▼
                  Cosine Similarity
                         │
            ┌────────────┼────────────┐
            ▼            ▼            ▼
       Text Score    MBTI Score   Location Score
            │            │            │
            └────────────┼────────────┘
                         ▼
                   Hybrid Score
                         │
                         ▼
                  User Feedback
                         │
                         ▼
                  Acceptance Rate
                         │
                         ▼
                  Adaptive Score
                         │
                         ▼
                  Ranked Matches