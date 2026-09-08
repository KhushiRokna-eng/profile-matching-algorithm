# Profile Matching Algorithm

A Python-based intelligent profile matching system that recommends compatible users by combining **NLP-based profile similarity, MBTI personality compatibility, location compatibility, and user feedback**.

The project is designed as a hybrid recommendation system where multiple sources of compatibility are combined into a single score to rank potential matches.

---

## 📌 Project Overview

Traditional recommendation systems often rely on a single type of information. This project explores a **hybrid profile matching approach** that considers both professional and personal characteristics.

Each user profile contains:

- Personal description
- Professional summary
- MBTI personality type
- Location

The system processes this information and calculates compatibility between users.

The matching process combines:

1. **Profile Text Similarity** using TF-IDF and Cosine Similarity
2. **MBTI Compatibility** based on personality dimensions
3. **Location Compatibility**
4. **Hybrid Compatibility Score**
5. **Adaptive Score** using previous user feedback

---

## 🎯 Objective

The main objective is to develop a profile matching algorithm capable of identifying users who are compatible based on their:

- Professional interests and career goals
- Personality traits
- Work style and personal interests
- Geographic location
- Previous interaction behavior

The system is designed to demonstrate how multiple compatibility signals can be combined into a single recommendation score.

---

## 🧠 System Architecture

```text
                User Profiles
                     │
                     ▼
            Profile Preprocessing
                     │
                     ▼
          TF-IDF Text Representation
                     │
                     ▼
          Cosine Text Similarity
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
            Previous Feedback
                     │
                     ▼
            Acceptance Rate
                     │
                     ▼
              Adaptive Score
                     │
                     ▼
          ┌──────────────────┐
          │  Matching Engine │
          └──────────────────┘
                     │
                     ▼
             Ranked Matches