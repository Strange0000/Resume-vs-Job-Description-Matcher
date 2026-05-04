# Resume vs Job Description Matcher

## Overview
This project is a simple Python program that compares a resume with a job description and calculates a match score based on keyword overlap.

The objective is to demonstrate **problem-solving ability, text processing, and logical implementation** without using external APIs or pretrained models.

---

## Features
- Text preprocessing:
  - Lowercasing
  - Punctuation removal
  - Stopword filtering
- Keyword extraction using sets
- Match score calculation (0–100)
- Identification of:
  -  Matching keywords
  -  Missing keywords

---

##  Approach

### 1. Text Cleaning
- Convert text to lowercase
- Remove punctuation using regex
- Split into words
- Remove common stopwords

### 2. Keyword Extraction
- Convert cleaned words into a **set** to ensure uniqueness

### 3. Matching Logic
- Matching keywords → intersection of sets
- Missing keywords → difference of sets

### 4. Match Score Formula

Match Score = (Matched Keywords / Total Job Keywords) × 100

---

##  Example

### Resume

Python developer with experience in machine learning, data analysis,
and building web applications using Flask and Django.


### Job Description

Looking for a Python developer skilled in Django, REST APIs,
machine learning, and cloud deployment.


### Output

Match Score: 57.14%
Matched Keywords: ['django', 'learning', 'machine', 'python']
Missing Keywords: ['apis', 'cloud', 'deployment', 'rest']


---

##  How to Run

### 1. Clone the repository

git clone https://github.com/your-username/resume-matcher.git

cd resume-matcher


### 2. Run the script

python main.py



##  Author
**Sumit Jaiswal**

---


