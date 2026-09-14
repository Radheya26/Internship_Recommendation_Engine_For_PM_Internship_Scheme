# 🤖 AI-Based Internship Recommendation Engine
### For PM Internship Scheme | Smart India Hackathon 2026 (Internal Round)

> An AI-powered internship recommendation system that understands student preferences and recommends the most relevant internship opportunities using semantic similarity.

---

## 📌 Overview

Finding the right internship can be challenging for students and freshers because internship opportunities are often scattered across large datasets and require manual searching.

The **AI-Based Internship Recommendation Engine** addresses this problem by taking a student's:

- 📍 Preferred Location
- 🏢 Sector
- 🎓 Field
- 💡 Skills

as input and intelligently matching them with relevant internship opportunities.

Instead of relying only on traditional keyword-based filtering, the system uses **semantic embeddings and vector similarity** to understand the contextual relationship between user preferences and internship information.

---

## 🎯 Problem Statement

Students and freshers often find it difficult to discover suitable internship opportunities matching their:

- Location
- Sector
- Field
- Skill set

This is mainly due to:

- Scattered and unstructured internship data
- Lack of intelligent matching
- Time-consuming manual searching

As a result, students may miss relevant opportunities even when suitable internships are available.

---

## 💡 Objective

The objective of this project is to build an AI-powered Internship Recommendation Engine that:

1. Takes user preferences as input.
2. Converts internship information and user queries into semantic embeddings.
3. Calculates similarity between the user query and available internships.
4. Ranks internships according to their relevance.
5. Displays the best matching opportunities through an interactive interface.

### 🎯 Goal

> Empower students with personalized, relevant, and high-quality internship suggestions aligned with their interests and career goals.

---

# 🏗️ System Architecture

The system follows a semantic-search-based recommendation pipeline:

```text
                 ┌─────────────────────┐
                 │   Internship Data   │
                 │      (Kaggle)       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Data Preparation  │
                 │ Cleaning & Enrichment│
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │      FastEmbed      │
                 │ Embedding Generation│
                 └──────────┬──────────┘
                            │
                            ▼
                    Pre-computed
                  Internship Vectors
                            │
                            │
┌─────────────────┐         │
│   User Inputs   │         │
│                 │         │
│ Location        │         │
│ Sector          │         │
│ Field           │         │
│ Skills          │         │
└────────┬────────┘         │
         │                  │
         ▼                  │
┌─────────────────────┐     │
│   Query Embedding   │     │
│      FastEmbed      │     │
└──────────┬──────────┘     │
           │                │
           └───────┬────────┘
                   ▼
          ┌──────────────────┐
          │ Similarity Match │
          │     NumPy Dot    │
          └─────────┬────────┘
                    │
                    ▼
          ┌──────────────────┐
          │  Ranked Results  │
          │ Top Internships  │
          └─────────┬────────┘
                    │
                    ▼
          ┌──────────────────┐
          │ Streamlit UI     │
          │ Recommendations  │
          └──────────────────┘
```

---

# ⚙️ Technology Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Core programming language |
| ⚡ FastAPI | Backend API |
| 🎨 Streamlit | Interactive frontend |
| 🧠 FastEmbed | Semantic embedding generation |
| 🔢 NumPy | Vector similarity computation |
| 📊 Kaggle Dataset | Internship data source |
| ⚡ uv | Python project and dependency management |

---

# 🔄 How It Works

## 1. Internship Data Preparation

The internship dataset is prepared before the recommendation process.

The dataset contains relevant information required for matching internships with student preferences, including:

- Location
- Sector
- Field
- Skills
- Detailed description

The internship information is then converted into semantic embeddings using **FastEmbed**.

These pre-computed embeddings are stored for efficient recommendation retrieval.

---

## 2. User Input

The user provides their preferences through the Streamlit interface:

```text
Preferred Location
        +
      Sector
        +
       Field
        +
      Skills
```

These preferences are combined to form a meaningful query.

---

## 3. Query Embedding

The user's query is converted into a semantic vector using FastEmbed.

The same embedding approach is used for the internship data, allowing the system to compare the user's requirements with available opportunities in the same vector space.

---

## 4. Similarity Matching

The query vector is compared with the pre-computed internship vectors.

NumPy is used to perform vector operations and calculate similarity using the dot product.

```text
User Query
    ↓
Query Embedding
    ↓
Compare With Internship Embeddings
    ↓
Similarity Scores
    ↓
Ranking
```

---

## 5. Recommendation

Internships are ranked according to their similarity with the user's requirements.

The system returns the most relevant internship opportunities, which are then displayed through the Streamlit interface.

---

# 🖥️ User Flow

```text
Start
  │
  ▼
Enter Preferences
  │
  ├── Location
  ├── Sector
  ├── Field
  └── Skills
  │
  ▼
Generate Query Embedding
  │
  ▼
Compare With Internship Embeddings
  │
  ▼
Calculate Similarity
  │
  ▼
Rank Internships
  │
  ▼
Display Recommended Internships
  │
  ▼
Explore Relevant Opportunities
```

---

# ✨ Key Features

### 🎯 Personalized Recommendations

Recommendations are generated according to the user's preferred location, sector, field, and skills.

### 🧠 Semantic Matching

FastEmbed enables the system to compare the contextual meaning of user requirements with internship information.

### ⚡ Efficient Recommendation

Pre-computed internship embeddings reduce the computational work required during each recommendation request.

### 🔎 Ranked Results

Internship opportunities are ranked according to their similarity with the user's preferences.

### 🎨 Interactive Interface

Streamlit provides a simple interface for entering preferences and viewing recommendations.

### 🔄 Updatable Dataset

The recommendation system can be updated when new internship data becomes available by processing the updated dataset and generating new embeddings.

---

# 📊 Dataset

The project uses an internship dataset obtained from Kaggle.

The dataset is prepared with relevant information for recommendation, including:

```text
Location
Sector
Field
Skills
Detailed Description
```

### Dataset Reference

```text
/datasets/everydaycoding/internship-opportunities-dataset
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Radheya26/Internship_Recommendation_Engine_For_PM_Internship_Scheme.git
cd Internship_Recommendation_Engine_For_PM_Internship_Scheme
```

---

## 2. Install Dependencies

This project uses **uv** for Python project and dependency management.

Install the project dependencies using:

```bash
uv sync
```

This will create or use the project's virtual environment and install the dependencies defined by the project.

---

# ▶️ Running the Project

The application consists of a **Streamlit frontend** and a **FastAPI backend**.

## Start the FastAPI Backend

The FastAPI backend is located inside the `src` directory:

```text
src/backend.py
```

First, navigate into the `src` directory:

```bash
cd src
```

Then start the FastAPI server:

```bash
uv run uvicorn backend:app --reload
```

The FastAPI backend will start and handle recommendation requests from the frontend.

> **Note:** Run the backend command from inside the `src` directory.

---

## Start the Streamlit Frontend

The Streamlit frontend is located at the project root:

```text
app.py
```

Open a **new terminal** from the project root and run:

```bash
uv run streamlit run app.py
```

The Streamlit interface will then be available in your browser.

---

# 🔌 Application Flow

```text
                 ┌─────────────────────┐
                 │       app.py        │
                 │  Streamlit Frontend │
                 └──────────┬──────────┘
                            │
                            │ User Preferences
                            ▼
                 ┌─────────────────────┐
                 │    backend.py       │
                 │      FastAPI        │
                 │      (src/)         │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │      FastEmbed      │
                 │  Query Embedding    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │       NumPy         │
                 │ Similarity Matching │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Ranked Internships │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │       app.py        │
                 │   Display Results   │
                 └─────────────────────┘
```

---

# 🛡️ Feasibility & Viability

## 🔧 Technical Feasibility

- Internship data can be processed into a structured format.
- FastEmbed provides semantic embedding generation.
- NumPy enables efficient vector operations.
- FastAPI provides a lightweight backend API.
- Streamlit provides an interactive user interface.
- The overall system can be deployed using commonly available computing infrastructure.

## ⚙️ Operational Viability

- Simple interface for students.
- Automated recommendation process.
- Minimal manual intervention during recommendation.
- Internship data can be periodically updated.

## 💰 Economic Viability

The project primarily relies on open-source technologies such as:

- Python
- FastAPI
- Streamlit
- FastEmbed
- NumPy

This helps keep the software infrastructure cost relatively low.

---

# ⚠️ Potential Challenges & Mitigation

| Challenge | Mitigation |
|-----------|------------|
| Data Quality | Data cleaning and enrichment |
| Limited Matching | Semantic similarity improves contextual matching |
| Growing Dataset | Pre-computed embeddings and efficient vector operations |
| Different User Queries | Semantic embeddings help handle variations in wording |

---

# 🌍 Impact & Benefits

## 👨‍🎓 Students & Freshers

- Faster discovery of relevant internships
- Personalized recommendations
- Reduced manual searching
- Better alignment between skills and opportunities

## 🏫 Educational Institutions

- Helps students discover suitable internship opportunities
- Supports informed career and internship decisions

## 🇮🇳 PM Internship Scheme

- Improves accessibility and discoverability of internship opportunities
- Helps students identify opportunities relevant to their profiles

## 🏢 Organizations

- Helps connect internship opportunities with students whose interests and skills are relevant to them

---

# 📈 Key Impact Areas

### 🔎 Better Discovery

Students can discover relevant internship opportunities without manually searching through large datasets.

### 🎯 Smarter Matching

Semantic similarity allows the system to go beyond simple keyword matching.

### ⏱️ Saves Time

Automated recommendations reduce the time and effort required to find suitable internships.

### 📚 Career Development

Students can discover opportunities that align with their skills, interests, and career goals.

### 🌐 Accessibility

A simple digital interface can make internship discovery easier for a wider range of students.

---

# 🔮 Future Scope

The current system can be further enhanced with:

- 👤 Resume-based personalization
- 🔎 Hybrid keyword + semantic search
- ⭐ User feedback-based recommendation improvement
- 📊 Larger and more diverse internship datasets
- 🔄 Integration with real-time internship opportunities
- 🧠 More advanced ranking and recommendation models

---

# 🔬 Research & Validation

The development approach follows the pipeline:

```text
Data Collection
      ↓
Data Preparation
      ↓
Embedding Generation
      ↓
Similarity Matching
      ↓
Recommendation Ranking
      ↓
System Evaluation
```

The system can be evaluated using different combinations of:

- Locations
- Sectors
- Fields
- Skills

to assess the relevance and quality of the recommendations.

---

# 🏆 Smart India Hackathon 2026 (Internal Round)

**Problem Domain:** PM Internship Scheme

**Project:** AI-Based Internship Recommendation Engine

**Team:** Radheya

**Team Leader:** Pritam Pramanik

**Institution:** Calcutta University

**Event:** Smart India Hackathon 2026

---

# 📜 Vision

> To make internship discovery intelligent, personalized, and accessible — helping every student find opportunities that genuinely match their skills, interests, and aspirations.

---

## 🙏 Acknowledgement

This project was developed as part of **Smart India Hackathon 2026 (Internal Round)** with the objective of improving internship discovery and recommendation for students under the PM Internship Scheme.

---
